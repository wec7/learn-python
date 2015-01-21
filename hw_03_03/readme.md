(c) 2014 Baruch College, MTH 9815.

Created on Oct 2, 2014

Author:

	Weiyi Chen, Yun Peng

Contact: 

	weiyi.alan.chen@gmail.com, yunpeng0101@gmail.com

Summary: 

	1. readme.md for crossing_bridge

	2. Crossing the Bridge. A group of n people wish to cross a bridge 
	at night. At most two people may cross at any time, and each group must 
	have a flashlight. Only one flashlight is available among the n people, 
	so some sort of shuttle arrangement must be arranged in order to return 
	the flashlight so that more people may cross. 
	Each person has a different crossing speed; the speed of a group is 
	determined by the speed of the slower member. This program is to determine a 
	strategy that gets all n people across the bridge in the minimum time.

Module:

	1. unittest: main(), TestCase
	2. sys: argv

Design:

	1. main(): read file into a list of lines, transfer to solve() 

	2. init(): initialize the people speed from file to a list for each test

	3. solve(): main structure of this whole file, deal with simpliest case first 
		and then general cases

	4. cal(): calculate the whole time taken to cross bridges

	5. printSequence(): print the required sequence, how people cross bridge with one light

Usage:

	python test_crossing_bridge.py
	python test_hand.py input_file.txt
