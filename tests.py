# -*- coding: utf-8 -*-

import unittest

from stats import Pair, Stats


class TestStats(unittest.TestCase):
    def setUp(self):
        self.results = [Pair('with', 'with')] * 40 + [Pair('with', 'without')] * 40 + [Pair('without', 'with')] * 10 + [Pair('without', 'without')] * 10
        self.stats = Stats(self.results)
            
    def test_stats(self):
        self.assertEquals(self.stats.total, 100)
        self.assertEquals(self.stats.err1t, 40)
        self.assertEquals(self.stats.err2t, 10)
        self.assertEquals(self.stats.correct, 50)
        self.assertEquals(self.stats.precision, 0.5)
        self.assertEquals(self.stats.recall, 0.8)
        self.assertEquals(self.stats.f1, 0.8/1.3)


if __name__ == '__main__':
    unittest.main()