#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing.dummy import Pool as ThreadPool
from collections import namedtuple

from text_classifier.regex_text_classifier import RegexTextClassifier
from file_classifier import classify_file
from base import Base


pool = ThreadPool(4)

base = Base({'with': 'images/with', 'without': 'images/without'})

regex_text_classifier = RegexTextClassifier(base.get_class_names(), 'with')

Pair = namedtuple('Pair', ('correct', 'answer'))
make_pair = lambda filename, correct: Pair(correct=correct, answer=classify_file(filename, regex_text_classifier))

results = pool.map(lambda filename: make_pair(filename, 'with'), base.get_class('with')[:5])

pool.close()
pool.join()

print results