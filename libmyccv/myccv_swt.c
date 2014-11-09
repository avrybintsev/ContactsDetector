#include "ccv.h"
#include "ccv_internal.h"
#include "myccv_swt.h"
#include <tesseract/capi.h>

int myccv_swt_detect_words_from_file(const void* filename, const ccv_swt_param_t params, ccv_array_t** words) {
	ccv_enable_default_cache();
	ccv_dense_matrix_t* image = 0;
	ccv_read(filename, &image, CCV_IO_GRAY | CCV_IO_ANY_FILE);
	if (image != 0)
	{
		*words = ccv_swt_detect_words(image, params);
		ccv_matrix_free(image);
	} else {
		*words = 0;
	}
	ccv_drain_cache();
	return *words == 0 ? -1 : 0;
}

int myccv_swt_recognize_words_from_file(const void* filename, const ccv_swt_param_t params, struct myccv_buffer* buf)
{
	TessBaseAPI* tesseract = TessBaseAPICreate();
	if (TessBaseAPIInit3(tesseract, 0, "eng+rus") != 0) {
		return -1;
	}		

	ccv_dense_matrix_t* image = 0;
	ccv_read(filename, &image, CCV_IO_GRAY | CCV_IO_ANY_FILE);
	if (image == 0) {
		return -1;
	}

	ccv_array_t* seq = ccv_swt_detect_words(image, params);
	//float width = image->cols, height = image->rows;
	if (seq  == 0)
	{
		ccv_matrix_free(image);
		return -1;
	}

	if (seq->rnum > 0)
	{
		int i;

		buf->len = 192 + seq->rnum * 131 + 2;
		char* data = (char*)malloc(buf->len);
		data[0] = '[';
		buf->written = 1;
		
		for (i = 0; i < seq->rnum; i++)
		{
			char cell[1024];
			ccv_rect_t* rect = (ccv_rect_t*)ccv_array_get(seq, i);

			char empty[] = "";
			char* word = TessBaseAPIRect(tesseract, image->data.u8, 1, image->step, rect->x, rect->y, rect->width, rect->height);
			if (!word)
				word = empty;
			int wordlen = strlen(word); 
			int j;
			for (j = 0; j < wordlen; j++)
				if (word[j] == '\n')
					word[j] = ' ';
			// 	if (!((word[j] >= 'a' && word[j] <= 'z') ||
			// 				(word[j] >= 'A' && word[j] <= 'Z') ||
			// 				(word[j] >= '0' && word[j] <= '9') ||
			// 				word[j] == ' ' ||
			// 				word[j] == '-')) // replace unsupported char to whitespace
			// 			word[j] = ' ';
			for (j = wordlen - 1; j >= 0 && word[j] == ' '; j--); // remove trailing whitespace
			word[j + 1] = 0, wordlen = j + 1;
			for (j = 0; j < wordlen && word[j] == ' '; j++); // remove leading whitespace
			wordlen -= j;
			memmove(word, word + j, wordlen + 1);
			if (wordlen > 512) // if the wordlen is greater than 512, trim it
				word[512] = 0;
			snprintf(cell, 1024, "{\"x\":%d,\"y\":%d,\"width\":%d,\"height\":%d,\"word\":\"%s\"}", rect->x, rect->y, rect->width, rect->height, word);

			size_t len = strnlen(cell, 1024);
			while (buf->written + len + 1 >= buf->len)
			{
				buf->len = (buf->len * 3 + 1) / 2;
				data = (char*)realloc(data, buf->len);
			}
			memcpy(data + buf->written, cell, len);
			buf->written += len + 1;
			data[buf->written - 1] = (i == seq->rnum - 1) ? ']' : ',';

		}

		buf->data = data;
		buf->len = buf->written;

	} else {

		buf->data = 0;
		buf->len = 0;
		buf->written = 0;

	}
	
	TessBaseAPIDelete(tesseract);
	ccv_matrix_free(image);
	ccv_array_free(seq);
	return 0;
}
