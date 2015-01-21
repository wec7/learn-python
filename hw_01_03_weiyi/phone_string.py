'''

(c) 2014 Baruch College, MTH 9815.

Created on Sep 6, 2014

@author: Weiyi Chen, Yun Peng
@contact: weiyi.alan.chen@gmail.com, yunpeng0101@gmail.com
@summary: Write a program phone_string.py that given a 10 digit phone number 
	(-n 2125551212), prints out all the possible strings that can be derived 
	from that number.
@usage: python phone_string.py -n <PHONE_NUMBER>

'''

#Python imports
import sys, getopt
from itertools import product

#3rd party imports
import pandas as pd 


def read_args(ls_argv):
	'''
	@summary: read arguments from command line
	@param ls_argv: list of auguments from command line
	@return str_phoneNum: -n for a 10 digit phone number (-n 2125551212)
	'''
	try:
		ls_opts, ls_args = getopt.getopt(ls_argv,"hn:")
	except getopt.GetoptError:
		print "usage: python phone_string.py -n <PHONE_NUMBER>"
		sys.exit(2)
	for str_opt, str_arg in ls_opts:
		if str_opt in ("-h"):
			print "usage: python phone_string.py -n <PHONE_NUMBER>"
			sys.exit()
		elif str_opt in ("-n"):
			str_phoneNum = str_arg
	return str_phoneNum


def print_phone_strings(str_phoneNum, ls_letterDistribute):
	'''
	@summary: prints out all the possible strings that can be derived phoneNum
	@param str_phoneNum: -n for a 10 digit phone number (-n 2125551212)
	@param ls_letterDistribute: letter distribution per digit according to
		given image
	'''
	ls_args = []
	for str_num in str_phoneNum:
		if str_num != '0' and str_num != '1':
			ls_args.append(ls_letterDistribute[int(str_num)])
	for i in product(*ls_args):
		print ''.join(i)


if __name__ == "__main__":
	str_phoneNum = read_args(sys.argv[1:])
	ls_letterDistribute = ['','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
	print_phone_strings(str_phoneNum, ls_letterDistribute)
	
		