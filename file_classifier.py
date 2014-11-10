# -*- coding: utf-8 -*-

from ccv import recognize_words_from_file


def classify_file(file_name, text_classifier):
	text = ''.join(map(lambda item: item.word, recognize_words_from_file(file_name)))
	return text_classifier.classify(text)
