# -*- coding: utf-8 -*-

class TextClassifier:
	def __init__(self, class_names, target_class):
		assert len(class_names) == 2
		self.class_names = class_names
		self.target_class = target_class
		self.second_class = class_names[0] if class_names[1] == target_class else class_names[1]

	def classify(self, text):
		raise NotImplementedError("Class %s doesn't implement classify()" % (self.__class__.__name__))
