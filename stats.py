#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple


Pair = namedtuple('Pair', ('answer', 'correct'))


class Stats:
	def __init__(self, results):
		err1t_criteria = lambda pair: pair.answer == 'with' and pair.correct == 'without' 
		err2t_criteria = lambda pair: pair.answer == 'without' and pair.correct == 'with'

		self.total = len(results)
		self.correct = len(filter(lambda pair: pair.answer == pair.correct, results))
		self.err1t = len(filter(err1t_criteria, results))
		self.err2t = len(filter(err2t_criteria, results))

		tp = len(filter(lambda pair: pair.answer == 'with' == pair.correct, results))
		fp = self.err1t
		tn = len(filter(lambda pair: pair.answer == 'without' == pair.correct, results))
		fn = self.err2t

		self.recall = (tp + 0.0) / (tp + fn) if tp + fn else 0
		self.precision = (tp + 0.0) / (tp + fp) if tp + fp else 0
		self.f1 = (2.0 * self.precision * self.recall) / (self.precision + self.recall) if self.precision + self.recall else 0

	def __repr__(self):
		return 'Total: %d, Correct: %d, Errors-I: %d, Errors-II: %d' % (self.total, self.correct, self.err1t, self.err2t)
