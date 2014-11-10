# -*- coding: utf-8 -*-

import re

from text_classifier import TextClassifier


class RegexTextClassifier(TextClassifier):
    def classify(self, text):
        def preprocess_text(text):
            return text.replace(' ', '')

        regex = [
            re.compile(r'9\d\d'),
            re.compile(r'\+7'),
            re.compile(r'@'),
            re.compile(r'\d\d-\d\d-\d\d'),
            re.compile(r'ww'),
            re.compile(r'\.\w\w'),
            re.compile(r'\(\d\d\d\)'),
            re.compile(r'http'),
        ]

        _text = preprocess_text(text)
        for pattern in regex:
            if pattern.match(_text):
                return self.target_class
        return self.second_class
        
