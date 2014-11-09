#include "ccv.h"
#include "ccv_internal.h"
#include "myccv_swt.h"

int ccv_swt_detect_words_from_file(const void* filename, const ccv_swt_param_t params, ccv_array_t** words) {
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
