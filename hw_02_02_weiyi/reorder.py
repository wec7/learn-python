'''

(c) 2014 Baruch College, MTH 9815.

Created on Sep 14, 2014

@author: Weiyi Chen, Yun Peng
@contact: weiyi.alan.chen@gmail.com, yunpeng0101@gmail.com
@summary: Write a program called reorder.py that accepts 2 possible parameters,
	a file (-f) or an integer (-i). Order the given list ascending (either file
	or randomly generated) by only flipping the top N values of the list (N is 
	arbitrary). Print the intermediate steps.
@usage: python reorder.py -f <FILE_NAME> or python reorder.py -i <INTEGER>

'''

#Python imports
import argparse
import random

def read_args():
	'''
	@summary: read arguments from command line
	@return ls_numbers: a list from the file if specified, or with range i from
		command line
	'''
	parser = argparse.ArgumentParser()
	# If the file is specified, the program will read a file with only one line
	#	with comma separated integer values
	parser.add_argument('-f', action="store")
	# If the integer is specified (-i n), the program will generate a list with 
	#	range and then shuffle using random.shuffle it.
	parser.add_argument('-i', action="store", type=int)
	if parser.parse_args().f != None:
		ls_numbers = open(parser.parse_args().f).read().split(',')
		ls_numbers = [int(x) for x in ls_numbers]
	else:
		ls_numbers = range(parser.parse_args().i)
		random.shuffle(ls_numbers)
	return ls_numbers

def flip(ls_numbers, i_to):
	'''
	@summary: order the given list ascending by only flipping the top N values 
		of the list, by recursion
	@param ls_numbers: the list from read_args(), either file or randomly 
		generated
	@param i_to: a record index of ls_numbers that has been ordered
	'''
	if len(ls_numbers[:i_to]) == 1:
		return ls_numbers
	i_max = [i for i,x in enumerate(ls_numbers[:i_to]) if x == max(\
		ls_numbers[:i_to])][-1]
	if i_max != i_to-1:
		if i_max != 0:
			# bring the largest number not yet sorted to the top with one flip
			ls_numbers[:i_max+1] = ls_numbers[:i_max+1][::-1]
			print ls_numbers
		# take it down to its final position with one more
		ls_numbers[:i_to] = ls_numbers[:i_to][::-1]
		print ls_numbers
	#repeat this for the remaining numbers.
	flip(ls_numbers, i_to-1)

def main():
	'''
	@summary: main file, read arguments, print original list and flip with 
		printing intermediate process
	'''
	ls_numbers = read_args()
	print ls_numbers
	flip(ls_numbers, len(ls_numbers))

if __name__ == '__main__':
	main()