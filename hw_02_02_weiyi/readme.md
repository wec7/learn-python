(c) 2014 Baruch College, MTH 9815.

Created on Sep 14, 2014

Author:

	Weiyi Chen, Yun Peng

Contact: 

	weiyi.alan.chen@gmail.com, yunpeng0101@gmail.com

Summary: 

	1. readme.md for reorder.py

	2. Write a program called reorder.py that accepts 2 possible parameters,
	a file (-f) or an integer (-i). Order the given list ascending (either file
	or randomly generated) by only flipping the top N values of the list (N is 
	arbitrary). Print the intermediate steps.

Library:

	1. argparse: 
		ArgumentParser(): add_argument(), parse_args()
	2. random: shuffle()

Design:

	1. read_args(): read arguments from command line
	- If the file is specified, the program will read a file with only one line with comma separated integer values
	- If the integer is specified (-i n), the program will generate a list with range and them shuffle using random.shuffle it.

	2. flip(ls_numbers, i_to): order the given list ascending by only flipping the top N values of the list, by recursion

		It's a pancake sorting problem. The simplest pancake sorting algorithm requires at most 2n − 3 flips. In this algorithm, we bring the largest number not yet sorted to the top with one flip, and then take it down to its final position with one more, then repeat this for the remaining numbers.

	3. print original list and flip with printing intermediate process simutaneously

Usage:

	python reorder.py -f <FILE_NAME> or python reorder.py -i <INTEGER>
