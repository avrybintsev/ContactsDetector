# -*- coding: utf-8 -*-

from collections import namedtuple
from ctypes import create_string_buffer, c_double, c_char, cast, POINTER, pointer, addressof
import json
import ccv
import os


Word = namedtuple('Word', ('x', 'y', 'width', 'height', 'word'))


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
        create_string_buffer(filename, len(filename)+1), 
        get_default_swt_params(update_params),
        pointer(words_array),
    )
    return map(
	   lambda item: Word(x=item.x, y=item.y, width=item.width, height=item.height, word=None),
	   [cast(ccv_array_get(words_array, i), POINTER(ccv.ccv_rect_t)).contents for i in xrange(words_array.contents.rnum)]
    ) if status == 0 else []


def _recognize_words_from_file_to_json(filename, update_params={}):
    json_buffer = pointer(ccv.myccv_buffer())
    status = ccv.ccv_swt_recognize_words_from_file(
        create_string_buffer(filename, len(filename)+1),
        get_default_swt_params(update_params),
        json_buffer,
    )    
    if status == 0 and json_buffer and json_buffer.contents and json_buffer.contents.data:
        char_array = (c_char*json_buffer.contents.len).from_address(addressof(json_buffer.contents.data.contents))     
        return char_array[:json_buffer.contents.len]
    return '[]'

def recognize_words_from_file(filename, update_params={}):
    json_string = _recognize_words_from_file_to_json(filename, update_params)
    try:
        words = json.loads(json_string)
    except:
        words = []
    return map(lambda item: Word(x=item.get(u'x'), y=item.get(u'y'), width=item.get(u'width'), height=item.get(u'height'), 
        word=item.get(u'word').encode('utf-8')), words)
