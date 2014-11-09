from collections import namedtuple
from ctypes import create_string_buffer, c_double, cast, POINTER, pointer
import ccv
import os


Word = namedtuple('Word', ('x', 'y', 'width', 'height'))


def ccv_array_get(array, i):
    assert(isinstance(array, POINTER(ccv.ccv_array_t)))
    assert(isinstance(i, int))
    return array.contents.data + array.contents.rsize * i


def get_default_swt_params(update_params={}):
    params = ccv.ccv_swt_param_t()
    values = dict([
        ('interval', 1),
        ('min_neighbors', 1),
        ('scale_invariant', 0),
        ('same_word_thresh', (c_double * 2)(0.1, 0.8)),
        ('size', 3),
        ('low_thresh', 124),
        ('high_thresh', 204),
        ('max_height', 300),
        ('min_height', 8),
        ('min_area', 38),
        ('letter_occlude_thresh', 3),
        ('aspect_ratio', 8),
        ('std_ratio', 0.83),
        ('thickness_ratio', 1.5),
        ('height_ratio', 1.7),
        ('intensity_thresh', 31),
        ('distance_ratio', 2.9),
        ('intersect_ratio', 1.3),
        ('elongate_ratio', 1.9),
        ('letter_thresh', 3),
        ('breakdown', 1),
        ('breakdown_ratio', 1.0),
    ])
    values.update(update_params)    
    for k, v in values.iteritems():
        setattr(params, k, v) 

    return params


def detect_words_from_file(filename, update_params={}):
    words_array = pointer(ccv.ccv_array_t())
    status = ccv.ccv_swt_detect_words_from_file(
        create_string_buffer(filename, len(filename)+2), 
        get_default_swt_params(update_params),
        pointer(words_array),
    )
    return map(
	   lambda item: Word(x=item.x, y=item.y, width=item.width, height=item.height),
	   [cast(ccv_array_get(words_array, i), POINTER(ccv.ccv_rect_t)).contents for i in xrange(words_array.contents.rnum)]
    ) if status == 0 else []
