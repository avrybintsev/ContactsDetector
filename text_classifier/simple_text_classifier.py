# -*- coding: utf-8 -*-

from text_classifier import TextClassifier


class SimpleTextClassifier(TextClassifier):
    def classify(self, text):
        _parts = [
            '@', 
            '.ru', 'ww', '.com', '.ua',
            '+7', '925', '926', '921', '918', '916', '903', # ...
        ]
        for part in _parts:
            if part in text:
                return self.target_class
        return self.second_class
        
