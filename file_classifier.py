# -*- coding: utf-8 -*-

from ccv import recognize_words_from_file


class FileClassifier:
	def __init__(self, filename, text_classifier):
		self.filename = filename
		self.text_classifier = text_classifier

	def classify(self):
		text = ''.join(map(lambda item: item.word, recognize_words_from_file(self.filename)))
		return self.text_classifier.classify(text)
