(c) 2014 Baruch College, MTH 9815.

Created on Sep 6, 2014

Author:

	Weiyi Chen, Yun Peng

Contact: 

	weiyi.alan.chen@gmail.com, yunpeng0101@gmail.com

Summary: 

	1. readme.md for phone_string.py

	2. Write a program phone_string.py that given a 10 digit phone number 
	(-n 2125551212), prints out all the possible strings that can be derived 
	from that number.

Library:

	1. sys: exit(), argv
	2. getopt: getopt(), GetoptError
	3. pandas: DataFrame() 
	4. itertools: product()

Design:

	1. read_args(ls_argv): read arguments from command line

	2. construct list of letter distributions s_letterDistribute

	3. print_phone_strings(str_phoneNum, ls_letterDistribute): prints out all 
	the possible strings that can be derived phoneNum

		for each single digit (except 0 and 1) in the phone number:

			(i) find its letter distribution in ls_letterDistribute

			(ii) append the letter strings to ls_args for product()

			(iii) apply itertools.product() to derive all strings

			(iv) print out by .join()

Usage:

	python phone_string.py -n <PHONE_NUMBER>
