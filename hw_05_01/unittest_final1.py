"""
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: unittest to test arbitrage
Usage: python unittest_final1.py
Author: Weiyi Chen
"""

# Python import
import unittest
import numpy as np

# My own module import
from final1 import *

class OrderBookTestCase(unittest.TestCase):
	''' Unittest for the arbitrage module '''
	def test_init(self):
		''' test initialization '''
		in_file = open('input.txt','r')
		str_line = in_file.readline()
		na_dist, na_rate = init(i_currencyNum=3, input_file=in_file)
		self.assertEquals(na_dist[0,1,0],1.2)
		self.assertEquals(na_dist[0,2,0],0.89)
		self.assertEquals(na_dist[1,0,0],0.88)
		self.assertEquals(na_dist[1,2,0],5.1)
		self.assertEquals(na_dist[2,0,0],1.1)
		self.assertEquals(na_dist[2,1,0],0.15)

	def test_floyd(self):
		''' test floyd algorithm '''
		i_currencyNum = 3
		na_dist = np.array([[[0.,0.,0.],[1.2,0.,0.],[0.89,0.,0.]],
			[[0.88,0.,0.],[0.,0.,0.],[5.1,0.,0.]],
			[[1.1,0.,0.],[0.15,0.,0.],[0.,0.,0.]]])
		na_rate = np.array([[[0.,0.,0.],[ 0.,0.,0.],[ 0.,0.,0.]],
			[[ 1.,0.,0.],[ 0.,0.,0.],[ 1.,0.,0.]],
			[[ 2.,0.,0.],[ 2.,0.,0.],[ 0.,0.,0.]]])
		floyd(i_currencyNum, na_dist, na_rate)
		self.assertEquals(na_rate[0,0,0],0)
		self.assertEquals(na_rate[0,0,1],1)
		self.assertEquals(na_rate[0,0,2],2)
		self.assertEquals(na_rate[0,1,0],0)
		self.assertEquals(na_rate[0,1,1],2)
		self.assertEquals(na_rate[0,1,2],0)
		self.assertEquals(na_rate[0,2,0],0)
		self.assertEquals(na_rate[0,2,1],1)
		self.assertEquals(na_rate[0,2,2],0)

if __name__ == '__main__':
	unittest.main() # Run unittest
