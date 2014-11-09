import os
from ctypes import CDLL, c_int, c_uint64, c_void_p, c_size_t, c_char_p, c_char, c_double, POINTER, Structure

_libraries = {}
_libraries['libccv'] = CDLL('libmyccv.so')

uint64_t = c_uint64

class ccv_rect_t(Structure):
    pass
ccv_rect_t._fields_ = [
    ('x', c_int),
    ('y', c_int),
    ('width', c_int),
    ('height', c_int),
]
class ccv_array_t(Structure):
    pass
ccv_array_t._fields_ = [
    ('type', c_int),
    ('sig', uint64_t),
    ('refcount', c_int),
    ('rnum', c_int),
    ('size', c_int),
    ('rsize', c_int),
    ('data', c_void_p),
]

class ccv_swt_param_t(Structure):
    pass
ccv_swt_param_t._fields_ = [
    ('interval', c_int),
    ('min_neighbors', c_int),
    ('scale_invariant', c_int),
    ('direction', c_int),
    ('same_word_thresh', c_double * 2),
    ('size', c_int),
    ('low_thresh', c_int),
    ('high_thresh', c_int),
    ('max_height', c_int),
    ('min_height', c_int),
    ('min_area', c_int),
    ('letter_occlude_thresh', c_int),
    ('aspect_ratio', c_double),
    ('std_ratio', c_double),
    ('thickness_ratio', c_double),
    ('height_ratio', c_double),
    ('intensity_thresh', c_int),
    ('distance_ratio', c_double),
    ('intersect_ratio', c_double),
    ('elongate_ratio', c_double),
    ('letter_thresh', c_int),
    ('breakdown', c_int),
    ('breakdown_ratio', c_double),
]

class myccv_buffer(Structure):
    pass
myccv_buffer._fields_ = [
    ('written', c_size_t),
    ('len', c_size_t),
    ('data', POINTER(c_char))
]

ccv_swt_detect_words_from_file = _libraries['libccv'].myccv_swt_detect_words_from_file
ccv_swt_detect_words_from_file.restype = c_int
ccv_swt_detect_words_from_file.argtypes = [c_void_p, ccv_swt_param_t, POINTER(POINTER(ccv_array_t))]

ccv_swt_recognize_words_from_file = _libraries['libccv'].myccv_swt_recognize_words_from_file
ccv_swt_recognize_words_from_file.restype = c_int
ccv_swt_recognize_words_from_file.argtypes = [c_void_p, ccv_swt_param_t, POINTER(myccv_buffer)]

__all__ = ['ccv_rect_t', 'ccv_array_t', 'ccv_swt_param_t', 'myccv_buffer', 'ccv_swt_detect_words_from_file', 'ccv_swt_recognize_words_from_file']
