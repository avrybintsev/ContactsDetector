#!/usr/bin/python
# -*- coding: utf-8 -*-

from text_classifier.regex_text_classifier import RegexTextClassifier
from file_classifier import FileClassifier
from base import Base


base = Base({'with': 'images/with', 'without': 'images/without'})
regex_text_classifier = RegexTextClassifier(base.get_class_names(), 'with')

for filename in base.get_class('with')[:10]:
	print FileClassifier(filename, regex_text_classifier).classify()
