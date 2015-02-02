"""
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: You are taking part in a large project to automate operations 
	for Northeastern Exchange of Resources and Commodities (NEERC). Different 
	resources and commodities are traded on this exchange via public auction. 
	Each resource or commodity is traded independently of the others and your 
	task is to write a core engine for this exchange -- its order book. There 
	is a separate instance of an order book for each traded resource or 
	commodity and it is not your problem to get the correct orders into order 
	books. The order book instance you will be writing is going to receive the 
	appropriate orders from the rest of exchange system.
Usage: python final1.py
Author: Weiyi Chen
"""

# Python imports
import numpy as np 
import argparse

def read_arg():
	''' 
	@summary: read arguments from command line and return it
	@details: accept 2 parameters -i <input file> -o <output file>
	@return: parse arguments class
	'''
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', action="store", default="input.txt", type=str)
	parser.add_argument('-o', action="store", default="output.txt", type=str)
	return parser.parse_args()

def init(i_currencyNum, input_file):
	'''
	@summary: initialization of distance between each two currencies
	@param i_currencyNum: number of currencies
	@param input_file: input to read rates between each two currencies
	@return na_dist: numpy array of distance between two currencies
	@return na_rate: their immediate points so far
	'''
	na_dist = np.zeros((i_currencyNum,i_currencyNum,i_currencyNum))
	na_rate = na_dist.copy()
	for i in range(i_currencyNum):
		ls_splitline = [float(str_num) for str_num in input_file.readline().split()]
		for j in range(i_currencyNum):
			if j < i:
				na_dist[i,j,0], na_rate[i,j,0] = ls_splitline[j], i
			elif j > i: 
				na_dist[i,j,0], na_rate[i,j,0] = ls_splitline[j-1], i
	return na_dist, na_rate

def floyd(i_currencyNum, na_dist, na_rate):
	'''
	@summary: apply folyd algorithm to find two neariest points between two 
		currencies
	@param i_currencyNum: number of currencies
	@param na_dist: modified rates between two currencies
	@param na_rate: number of immediate points so far
	@return: none, but will update na_dist and na_rate
	'''
	for d in range(1,i_currencyNum,1):
		for k in range(i_currencyNum):
			for i in range(i_currencyNum):
				for j in range(i_currencyNum):
					if na_dist[i,j,d] < na_dist[i,k,d-1]*na_dist[k,j,0]:
						na_dist[i,j,d] = na_dist[i,k,d-1]*na_dist[k,j,0]
						na_rate[i,j,d] = k

def output(i,j,d,na_rate,out_file):
	'''
	@summary: print out the result according to the question requirement
	@details: For each table in the input file you must determine whether a 
		sequence of exchanges exists that results in a profit of more than 1 
		percent (0.01). If a sequence exists you must print the sequence of 
		exchanges that results in a profit. If there is more than one sequence 
		that results in a profit of more than 1 percent you must print a 
		sequence of minimal length, i.e., one of the sequences that uses the 
		fewest exchanges of currencies to yield a profit.
	@param i,j,d: dimention index of na_rate
	@param na_rate: number of immediate points between two currencies so far
	@return: none, but will print out required entry of na_rate
	'''
	if d == -1:
		print int(i+1),
		out_file.write(str(int(i+1))+' ')
	else:
		output(i, na_rate[i,j,d], d-1, na_rate, out_file)
		print int(j+1),
		out_file.write(str(int(j+1))+' ')

def solve(i_currencyNum, input_file, out_file):
	'''
	@summary: solve each case from input file
	@param i_currencyNum: number of currencies
	@param input_file: file containing inputs used to read original rates
	@return: none, this is the structure of soving each case
	'''
	na_dist, na_rate = init(i_currencyNum, input_file)
	floyd(i_currencyNum, na_dist, na_rate)
	for d in range(1,i_currencyNum,1):
		for i in range(i_currencyNum):
			if na_dist[i,i,d] > 1.01:
				output(i,i,d,na_rate,out_file)
				print 
				out_file.write('\n')
				return
	print "no arbitrage sequence exists"
	out_file.write("no arbitrage sequence exists\n")

def main():
	''' main file to read input and solve each case by sequence '''
	in_file = open(read_arg().i,'r')
	out_file = open(read_arg().o,'w')
	while True:
		str_line = in_file.readline()
		if str_line:
			solve(int(str_line), in_file, out_file)
		else:
			break

if __name__ == '__main__':
	main()