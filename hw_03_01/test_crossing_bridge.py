import unittest
from crossing_bridge import *

class BridgeTestCase(unittest.TestCase):
	''' unittest for crossing_bridge '''
	def runTest(self):
		self.test_init()
		self.test_cal()
	