#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing.dummy import Pool as ThreadPool
from collections import namedtuple

from text_classifier.regex_text_classifier import RegexTextClassifier
from file_classifier import classify_file
from base import Base
from stats import Pair
from report import excel_report


if __name__ == '__main__':
	pool = ThreadPool(4)

	base = Base({'with': 'images/with', 'without': 'images/without'})
	regex_text_classifier = RegexTextClassifier(base.get_class_names(), target_class='with')
	make_pair = lambda filename, correct: Pair(answer=classify_file(filename, regex_text_classifier), correct=correct)
	results = pool.map(lambda item: make_pair(item['file_name'], item['class_name']), list(base.iter_dicts())[:50] + list(base.iter_dicts())[::-1][:50])

	pool.close()
	pool.join()

	excel_report(results)
