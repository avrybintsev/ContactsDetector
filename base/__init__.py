#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join
from random import shuffle


class Base:
	def __init__(self, dirs):
		'''
			dirs should be a dict {'class_name': 'dir_containing_images_path', ...}
		'''
		self.dirs = dirs
		self.files = {
			k: [join(v, f) for f in listdir(v) if isfile(join(v, f)) and not f.startswith('.')] for k, v in dirs.iteritems()
		}

	def get_classes(self):
		return {k: len(v) for k, v in self.files.iteritems()}

	def get_class_names(self):
		return (k for k in self.files.iterkeys())

	def get_class(self, name):
		return self.files.get(name)

	def random_split(self, parts=5):
		indicies = {k: range(len(v)) for k, v in self.files.iteritems()}
		for k in indicies.iterkeys():
			shuffle(indicies[k])

		items_by_indicies = lambda ind, k: [self.files[k][index] for index in ind]
		return {
			k: [items_by_indicies(indicies[k][i::parts], k) for i in xrange(parts)] 
			for k, v in self.files.iteritems()
		}

	def cross_validation_split(self, parts=5):
		parts = self.random_split(parts)
		return [{
			'train': {k: v[j] for k, v in parts.iteritems()},
			'test': {k: sum([v[i] for i in xrange(parts) if i != j], []) for k, v in parts.iteritems()},
		} for j in xrange(parts)]

