struct myccv_buffer {
  size_t written;
  size_t len;
  void *data;
};

int myccv_swt_detect_words_from_file(const void* filename, const ccv_swt_param_t params, ccv_array_t** words);
int myccv_swt_recognize_words_from_file(const void* filename, const ccv_swt_param_t params, struct myccv_buffer* buf);
