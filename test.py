#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from ccv import detect_words_from_file, recognize_words_from_file, Word
from text_classifier.regex_text_classifier import RegexTextClassifier
from base import Base


class FileClassifier:
	def __init__(self, filename, text_classifier):
		self.filename = filename
		self.text_classifier = text_classifier

	def classify(self):
		text = ''.join(map(lambda item: item.word, recognize_words_from_file(filename)))
		return self.text_classifier.classify(text)

base = Base({'with': 'images/with', 'without': 'images/without'})
regex_text_classifier = RegexTextClassifier(base.get_class_names(), 'with')

for filename in base.get_class('with')[:10]:
	print FileClassifier(filename, regex_text_classifier).classify()
