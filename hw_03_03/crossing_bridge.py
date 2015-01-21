"""
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: Crossing the Bridge. A group of n people wish to cross a bridge 
	at night. At most two people may cross at any time, and each group must 
	have a flashlight. Only one flashlight is available among the n people, 
	so some sort of shuttle arrangement must be arranged in order to return 
	the flashlight so that more people may cross. 
	Each person has a different crossing speed; the speed of a group is 
	determined by the speed of the slower member. This program is to determine a 
	strategy that gets all n people across the bridge in the minimum time.
Usage: python crossing_bridge.py input_file.txt
Author: Weiyi Chen, Yun Peng
"""

# Python import
import sys

def init(ls_fileLine):
	'''
	@summary: initialize the people speed from file to a list for each test
	@param ls_fileLine: list of raw file lines
	@return: a list of people speed in one test
	'''
	i_peopleNum = int(ls_fileLine[0])
	ls_peopleSpeed = [int(speed) for speed in ls_fileLine[1:1+i_peopleNum]]
	ls_fileLine = ls_fileLine[1+i_peopleNum:]
	return sorted(ls_peopleSpeed)


def cal(ls_peopleSpeed):
	'''
	@summary: calculate the whole time taken to cross bridges
	@param ls_peopleSpeed: a list of sorted people speed
	@return: an integer indicating the minimum time to cross bridge
	'''
	i_sum = ls_peopleSpeed[1]
	for i in range(len(ls_peopleSpeed)-2, 1, -2):
		i_sum += min(ls_peopleSpeed[i+1]+ls_peopleSpeed[1]*2+ls_peopleSpeed[0],\
			ls_peopleSpeed[i+1]+ls_peopleSpeed[i]+ls_peopleSpeed[0]*2);
	if (len(ls_peopleSpeed)%2):
		i_sum += ls_peopleSpeed[0]+ls_peopleSpeed[2]
	return i_sum


def printSequence(ls_peopleSpeed):
	''' 
	@summary: print the required sequence, how people cross bridge with one light
	@param ls_peopleSpeed: a list of sorted people speed
	'''
	i_peopleNum = len(ls_peopleSpeed)
	for i in range(i_peopleNum-2,1,-2):
		if (ls_peopleSpeed[i+1]+ls_peopleSpeed[1]*2+ls_peopleSpeed[0] < \
			ls_peopleSpeed[i+1]+ls_peopleSpeed[i]+ls_peopleSpeed[0]*2):
			print ls_peopleSpeed[0], str(ls_peopleSpeed[1])+'\n', str(ls_peopleSpeed[0])
			print ls_peopleSpeed[i], str(ls_peopleSpeed[i+1])+'\n', str(ls_peopleSpeed[1])
		else:
			print ls_peopleSpeed[0], str(ls_peopleSpeed[i+1])+'\n', str(ls_peopleSpeed[0])
			print ls_peopleSpeed[0], str(ls_peopleSpeed[i])+'\n', str(ls_peopleSpeed[0])
	if (i_peopleNum % 2):
		print ls_peopleSpeed[0], str(ls_peopleSpeed[2])+'\n', str(ls_peopleSpeed[0])+'\n'
	print ls_peopleSpeed[0], ls_peopleSpeed[1]


def solve(ls_peopleSpeed):
	'''
	@summary: main structure of this whole file, deal with simpliest case first 
		and then general cases
	@param ls_peopleSpeed: a list of sorted people speed
	'''
	if (len(ls_peopleSpeed) == 1):
		print str(ls_peopleSpeed[0])+'\n', str(ls_peopleSpeed[0])
	elif (len(ls_peopleSpeed) == 2):
		print str(ls_peopleSpeed[1])+'\n', str(ls_peopleSpeed[0]), str(ls_peopleSpeed[1])
	else:
		print cal(ls_peopleSpeed)
		printSequence(ls_peopleSpeed)


def main(str_inputFile):
	'''
	@summary: read file into a list of lines, transfer to solve() 
	@param str_inputFile: the input file name 
	'''
	f_inputFile = open(str_inputFile, 'r')
	ls_fileLine = [str_line for str_line in f_inputFile.readlines()]
	i_cashNum, ls_fileLine = int(ls_fileLine[0]), ls_fileLine[2:]
	for i in range(i_cashNum, 0, -1):
		solve(init(ls_fileLine))


if __name__ == '__main__':
	main(sys.argv[1])