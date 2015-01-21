"""
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: unittest to test crossing_bridge.py
Usage: python test_crossing_bridge.py
Author: Weiyi Chen, Yun Peng
"""

# Python import
import unittest

# Test module import
from crossing_bridge import *

class BridgeTestCase(unittest.TestCase):
	''' unittest for crossing_bridge '''
	def runTest(self):
		''' run all unittests '''
		self.test_init()
		self.test_cal()

	def test_init(self):
		''' compare output of init() and expected output
			should be able to convert str to int and sort
		'''
		self.assertEquals(init(['4', '1', '2', '6', '10']), [1, 2, 6, 10])
		self.assertEquals(init(['4', '1', '5', '2', '10']), [1, 2, 5, 10])
		self.assertEquals(init(['4\n', '1\n', '5\n', '2\n', '10']), [1, 2, 5, 10])

	def test_cal(self):
		''' compare output of cal() and expected output, algorithm test '''
		self.assertEquals(cal([1,1,1,1]), 5)
		self.assertEquals(cal([1,2,5,10]), 17)
		self.assertEquals(cal([5,6,7,8]), 31)

if __name__ == '__main__':
	unittest.main()