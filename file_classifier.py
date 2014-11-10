# -*- coding: utf-8 -*-

from ccv import recognize_words_from_file


def classify_file(filename, text_classifier):
	text = ''.join(map(lambda item: item.word, recognize_words_from_file(filename)))
	return text_classifier.classify(text)
