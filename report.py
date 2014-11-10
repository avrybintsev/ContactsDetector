# -*- coding: utf-8 -*-

import xlwt
from collections import OrderedDict

from stats import Stats


def excel_report(results, file_name='results.xls'):
	stats = Stats(results)

	wb = xlwt.Workbook()
	ws = wb.add_sheet('Statistics')

	ws.write(0, 0, 'Contacts detection')

	def write_pairs(pairs, start_row=1):
		current = start_row
		for k, v in pairs.iteritems():
			ws.write(current, 0, k)
			ws.write(current, 1, v)
			current += 1

	write_pairs(OrderedDict((
		('Total', stats.total),
		('Correct', stats.correct),
		('Type I Errors', stats.err1t),
		('Type II Errors', stats.err2t),
		('Precision', stats.precision),
		('Recall', stats.recall),
		('F1-score', stats.f1),
	)))

	wb.save(file_name)
