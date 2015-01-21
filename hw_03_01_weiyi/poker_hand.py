"""
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: Compare several pairs of poker hands and to indicate which, 
	if either, has a higher rank. The program will receive an input file as 
	parameter. The file will contains several lines, each containing the 
	designation of ten cards: the first five cards are the hand for the player 
	named "Black" and the next five cards are the hand for the player named 
	"White".
Usage: python poker_hand.py <inputfile>
Author: Weiyi Chen, Yun Peng
"""

# Python import
import sys

# My own module import
from test_hand import HandTestCase

# Global parameters
BLACK, WHITE, TIE = range(3)
MESSAGE = {
	BLACK:	"Black wins.",
	WHITE:	"White wins.",
	TIE:	"Tie."
} 

def main(str_inputfile):
	'''
	@summary: main function to compare pairs of poker hands from <inputfile>
	@param str_inputfile: inputfile name from command line
	'''
	pokerHandTest = HandTestCase()
	inputfile = open(str_inputfile, 'r')
	for line in inputfile:
		print MESSAGE[pokerHandTest._winner(line[0:14], line[15:29])]

if __name__ == '__main__':
	main(sys.argv[1])