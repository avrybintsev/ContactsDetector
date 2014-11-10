# -*- coding: utf-8 -*-

class TextClassifier:
	def __init__(self, classes, target_class):
		assert len(classes) == 2
		self.classes = classes
		self.target_class = target_class
		self.second_class = classes[0] if classes[1] == target_class else classes[1]

	def classify(self, text):
		raise NotImplementedError("Class %s doesn't implement classify()" % (self.__class__.__name__))

	def is_target_class(self, class_name):
		return self.target_class == class_name
