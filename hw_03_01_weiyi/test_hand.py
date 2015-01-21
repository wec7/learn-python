"""
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: unittest to test hand class in hand.py
Usage: python test_hand.py
Author: Weiyi Chen, Yun Peng
"""

# Python import
import unittest

# My own module import
from hand import *

# Global variables
FIRST, SECOND, SPLIT = range(3)

class HandTestCase(unittest.TestCase):
    ''' Unittest for the hand module '''

    def runTest(self):
        ''' run all unittests '''
        self.test_hand_comparisons()

    def _winner(self, s1, s2):
        ''' compare poker hand s1 and poker hand s2 '''
        h1, h2 = Hand.from_str(s1), Hand.from_str(s2)
        if h1 > h2: return FIRST
        if h1 < h2: return SECOND
        return SPLIT

    def test_hand_comparisons(self):
        ''' set up all possible comparisons for unittests '''
        self.assertEquals(self._winner('Ac Qd Jh 4c 2c', 'Qd Tc 4h 6s 9d'), FIRST)
        self.assertEquals(self._winner('Ac Qd Jh 4c 2c', 'Ad Tc 4h 6s 9d'), FIRST)  # test kickers
        self.assertEquals(self._winner('Ac Qd Jh 4c 2c', 'Ad 8c Qh Js 9d'), SECOND) # test kickers
        self.assertEquals(self._winner('Ac Qd Jh 4c 2c', 'Ad Tc 4h As 9d'), SECOND)
        self.assertEquals(self._winner('2c 2d 4h 4c 8c', '2c 2d 4h 4c 8c'), SPLIT)
        self.assertEquals(self._winner('2c 2d 4h 4c 9c', '2c 2d 4h 4c 8c'), FIRST)  # test kickers
        self.assertEquals(self._winner('Ac Jc Kc Tc Qc', 'Ac Qd Jh 4c 2c'), FIRST)  # royal flush beats everything
        self.assertEquals(self._winner('Ac Jc Kc Tc Qc', 'Ac Ad 8h 7c Tc'), FIRST)
        self.assertEquals(self._winner('Ac Jc Kc Tc Qc', 'Ac Ad 8h 7c 7s'), FIRST)
        self.assertEquals(self._winner('Ac Jc Kc Tc Qc', '8c 8d 8h 7c Tc'), FIRST)
        self.assertEquals(self._winner('Ac Jc Kc Tc Qc', '8c 7d 6h 5c 4c'), FIRST)
        self.assertEquals(self._winner('Ac Jc Kc Tc Qc', 'Ac 2d 3h 4c 5c'), FIRST)
        self.assertEquals(self._winner('Ac Jc Kc Tc Qc', 'Ac Jd Kh Tc Qc'), SPLIT)
        self.assertEquals(self._winner('Ac Jc Kc Tc Qc', '8c 6c 5c Qc Jc'), FIRST)
        self.assertEquals(self._winner('Ac Jc Kc Tc Qc', '8c 8d 8h 6d 6h'), FIRST)
        self.assertEquals(self._winner('Ac Jc Kc Tc Qc', 'Qc Qd Qh Qs 6h'), FIRST)
        self.assertEquals(self._winner('Ac Jc Kc Tc Qc', 'Ah 4h 2h 3h 5h'), FIRST)
        self.assertEquals(self._winner('Ac Jc Kc Tc Qc', 'Ac Jc Kc Tc Qc'), SPLIT)
        self.assertEquals(self._winner('9c 8d 7h 6c 5c', '8c 7d 6h 5c 4c'), FIRST)  # high card in straights win
        self.assertEquals(self._winner('9c 8c 7c 6c 5c', '8c 7c 6c 5c 4c'), FIRST)  # high card in straight flushes win
        self.assertEquals(self._winner('Jc Js Td Th Tc', 'Qc Qd Qh Qs 6h'), SECOND) # 4-kind beats full house
        self.assertEquals(self._winner('Jc Js Jd Jh Tc', 'Qc Qd Qh Qs 6h'), SECOND) # higher rank in 4 of a kind wins
        self.assertEquals(self._winner('Ac As Ad 6h 6c', 'Qc Qd Qh Ts Th'), FIRST)  # higher rank in Fh wins
        self.assertEquals(self._winner('Ac As Ad 6h 6c', 'Ac Ad Ah Ts Th'), SECOND) # higher rank in Fh wins
        self.assertEquals(self._winner('Ac As Ad 6h 6c', 'Ac Ad Ah 6s 6h'), SPLIT)
        self.assertEquals(self._winner('6c Tc Qc 2c 9c', 'Kh 4h 9h Jh 8h'), SECOND) # high card in flush wins

if __name__ == '__main__':
    unittest.main() # Run unittest
