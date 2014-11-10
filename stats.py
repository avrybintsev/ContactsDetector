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

	def __repr__(self):
		return 'Total: %d, Correct: %d, Errors-I: %d, Errors-II: %d' % (self.total, self.correct, self.err1t, self.err2t)
