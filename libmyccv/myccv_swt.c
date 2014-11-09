#include "ccv.h"
#include "ccv_internal.h"

ccv_array_t* ccv_swt_detect_words_from_file(const void* filename, ccv_swt_param_t params) {
	ccv_enable_default_cache();
	ccv_dense_matrix_t* image = 0;
	ccv_read(filename, &image, CCV_IO_GRAY | CCV_IO_ANY_FILE);
	if (image != 0)
	{
		ccv_array_t* words = ccv_swt_detect_words(image, params);
		ccv_matrix_free(image);
		return words;
	}
	ccv_drain_cache();
	return 0;
}
