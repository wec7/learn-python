(c) 2014 Baruch College, MTH 9815.

Created on Oct 8, 2014

Author:

	Weiyi Chen, Yun Peng

Contact: 

	weiyi.alan.chen@gmail.com, yunpeng0101@gmail.com

Summary: 

	1. readme.md for coins.py (Nim game)

	2. Nim is a mathematical game of strategy in which two players take
	turns removing objects from distinct heaps. On each turn, a player must 
	remove at least one object, and may remove any number of objects provided 
	they all come from the same heap.
	The normal game is between two players and played with three heaps of any 
	number of objects. The two players alternate taking any number of objects 
	from any single one of the heaps. The goal is to be the last to take an 
	object. In misère play, the goal is instead to ensure that the opponent is 
	forced to take the last remaining object.

Module:

	1. os: remove() to remove files on given path
	2. sys: argv to read arguments from cmd line
	3. time: sleep() to control the time for program to sleep
	4.

Design:

	1. Coins::__init__(): initialization of the game with players and board

	2. Coins::play(): escribe the process of the game

		2.1 Coins::read_command(): read commands from command line, mainly input and output directory

		2.2 Coins::pull_board(): update board from the other's file

		2.3 Coins::take_turn(): describe player's behavior in his turn

			2.3.1 Coins::create_move(): given current board status, create movement

			2.3.2 Coins::get_row(): get row number from create_move()

			2.3.3 Coins::get_int(): get the number of sticks to take from create_move()

		2.4 Coins::pull_board(): send board info to the other

	4. Coins::display_board(): show the current board information

Usage:

	python coins.py -s -i in/in.txt -o out/out.txt
	python coins.py -i out/out.txt -i in/in.txt
