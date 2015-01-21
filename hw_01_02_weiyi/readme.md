(c) 2014 Baruch College, MTH 9815.

Created on Sep 6, 2014

Author:

	Weiyi Chen, Yun Peng

Contact: 

	weiyi.alan.chen@gmail.com, yunpeng0101@gmail.com

Summary: 

	1. readme.md for optimal_change.py

	2. Create a program call optimal_change.py that takes an amount as 
	parameter (-m AMOUNT) and prints out the minimum number of bills and 
	coins in standard US denomination necessarily to represent that amount.

Library:

	1. sys: exit(), argv
	2. getopt: getopt(), GetoptError
	3. pandas: DataFrame() 

Design:

	1. read_args(ls_argv): read arguments from command line

	2. construct list of denominations ls_changes

	3. optimal_change(f_amount, ls_changes): calculate the minimum number of 
	bills and coins in standard US denomination

		(i) multiply the amount by 100 and round to integer

		for each denomination from large to small:

			(i) multiply denomination by 100 and change type to integer too

			(ii) # of denomination = amount / denomination

			(iii) update amount: amount = amount - # * denomination

			(iv) Record information necessary to the dataframe df_changes

	3. print out results df_changes

Usage:

	python optimal_change.py -m <AMOUNT>
