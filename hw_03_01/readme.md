(c) 2014 Baruch College, MTH 9815.

Created on Sep 14, 2014

Author:

	Weiyi Chen, Yun Peng

Contact: 

	weiyi.alan.chen@gmail.com, yunpeng0101@gmail.com

Summary: 

	1. readme.md for poker_hand

	2. Compare several pairs of poker hands and to indicate which, 
	if either, has a higher rank. The program will receive an input file as 
	parameter. The file will contains several lines, each containing the 
	designation of ten cards: the first five cards are the hand for the player 
	named "Black" and the next five cards are the hand for the player named 
	"White".

Module:

	1. unittest: main(), TestCase
	2. my own mudule: card, hand, test_hand

Design:

	1. card module: A playing card; e.g. ace of hearts
		- __init__(): val is a value in [0,52) where [0,12] represents the 2-A ranks
			in the diamonds suit, [13,25] hearts, [26-38] clubs, and [39,51] spades.
		- __cmp__(): Cards are compared by their rank alone
		- __str__(): Essentially describe
		- from_str(): return Card instance from a short format string representation 
			of the card such as Ac or 3D

	2. hand module: A set of cards with support for determining which poker hand
		the cards form.  Also supports comparing two hands for determining
		who 'wins' in a showdown. Note that the analysis performed searches
		for the *best* possible poker hand.  
		- __init__(): initialize
		- from_str(): Creates a hand from a string like Ad Th 3s 5c 7d
		- add(): adds a card to the hand. avoid accessing the cards directly
		- get_type(): returns one of HIGHCARD, PAIR, etc. and requires 5 cards in the hand
		- __cmp__(): compare hands following standard poker hand rankings, including kickers.
		- _analyze(): determine the best hand possible given the current set of cards

	3. test_hand module: unittest for the hand module
		- runTest(): basic function of unittest
		- _winner(): compare poker hands
		- test_hand_comparisons(): set up all possible comparisons for unittests

Usage:

	python test_hand.py
	python poker_hand.py inputfile.txt
