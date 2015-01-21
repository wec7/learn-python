'''

(c) 2014 Baruch College, MTH 9815.

Created on Sep 6, 2014

@author: Weiyi Chen, Yun Peng
@contact: weiyi.alan.chen@gmail.com, yunpeng0101@gmail.com
@summary: Create a program call optimal_change.py that takes an amount as 
	parameter (-m AMOUNT) and prints out the minimum number of bills and 
	coins in standard US denomination necessarily to represent that amount.
@usage: python optimal_change.py -m <AMOUNT>

'''

#Python imports
import sys, getopt
#3rd party imports
import numpy as np 
import pandas as pd 


def read_args(ls_argv):
	'''
	@summary: read arguments from command line
	@param ls_argv: list of auguments from command line
	@return f_amount: -m for an amount (like -m 10.23)
	'''
	try:
		ls_opts, ls_args = getopt.getopt(ls_argv,"hm:")
	except getopt.GetoptError:
		print "usage: python optimal_change.py -m <AMOUNT>"
		sys.exit(2)
	for str_opt, str_arg in ls_opts:
		if str_opt in ("-h"):
			print "usage: python optimal_change.py -m <AMOUNT>"
			sys.exit()
		elif str_opt in ("-m"):
			f_amount = float(str_arg)
	return f_amount


def optimal_change(f_amount, ls_changes):
	'''
	@summary: calculate the minimum number of bills and coins in standard US 
		denomination
	@param f_amount: an amount from command line (like -m 10.23)
	@param ls_changes: standard US denomination
	@return df_changes: number of bills for each denomination
	'''
	i_amount = int(f_amount*100)
	ls_numChanges = []
	for i in range(len(ls_changes)):
		i_change = int(ls_changes[i] * 100)
		ls_numChanges.append(i_amount/i_change)
		i_amount %= i_change
	d_changes = {'#': ls_numChanges}
	df_changes = pd.DataFrame(d_changes, index=ls_changes)
	return df_changes


if __name__ == "__main__":
	f_amount = read_args(sys.argv[1:])
	ls_changes = [100, 50, 20, 10 ,5, 1, 0.25, 0.1, 0.05, 0.01]
	print optimal_change(f_amount, ls_changes)
	