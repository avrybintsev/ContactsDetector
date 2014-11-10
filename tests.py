# -*- coding: utf-8 -*-

import unittest

from stats import Pair, Stats


class TestStats(unittest.TestCase):
    def setUp(self):
        self.results = [Pair('with', 'with')] * 10 + [Pair('with', 'without')] * 5 + [Pair('without', 'with')] * 5 + [Pair('without', 'without')] * 10
        self.stats = Stats(self.results)
            
    def test_stats(self):
        self.assertEquals(self.stats.total, 30)
        self.assertEquals(self.stats.err1t, 5)
        self.assertEquals(self.stats.err2t, 5)
        self.assertEquals(self.stats.correct, 20)


if __name__ == '__main__':
    unittest.main()