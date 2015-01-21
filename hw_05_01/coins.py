"""
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: Nim is a mathematical game of strategy in which two players take
	turns removing objects from distinct heaps. On each turn, a player must 
	remove at least one object, and may remove any number of objects provided 
	they all come from the same heap.
	The normal game is between two players and played with three heaps of any 
	number of objects. The two players alternate taking any number of objects 
	from any single one of the heaps. The goal is to be the last to take an 
	object. 
Usage: 
	Player 1: python coins.py -s -i in/in.txt -o out/out.txt
	Player 2: python coins.py -i out/out.txt -i in/in.txt
Author: Weiyi Chen, Yun Peng
"""

# python imports
import os
import time
import argparse
import sys
import copy

class Coins(object):
	''' Classes represents the whole game '''
	def __init__(self):
		'''
		@summary: initialization of the game
		@obj ls_players: represent the two players in the game
		@obj ls_board: represents the current board in the game, where the entries
			is the remaining sticks in the heap A,B,C respectively
		'''
		self.ls_players = ['P1', 'P2']
		self.ls_board   = [2, 5, 7]
	
	def play(self):
		'''
		@summary: describe the process of the game
		@str inputdir: input directory address, for P1 in/in.txt, for P2 opposite
		@str outputdir: outputdir directory address, for P2 out/out.txt, for P1 opposite
		'''
		inputdir, outputdir = self.read_command()
		b_first = True
		# Two players take turn to operate the game
		while True:
			for str_player in self.ls_players:
				# in P1's program with '-s' in commands, should pass P2's rounds
				if sys.argv[1] == '-s' and str_player == 'P2':
					print 'P2\'s Turn:'
					self.display_board()
					continue
				# in P2's program without '-s' in commands, should pass P1's rounds
				if sys.argv[1] != '-s' and str_player == 'P1':
					print "P1\'s Turn:"
					self.display_board()
					b_first = False
					continue
				self.take_turn(str_player, inputdir, outputdir, b_first)
				b_first = False
				# when the sum of board is 0, that means you win
				if sum(self.ls_board) == 0:
					print 'You ('+str_player + ') won!'
					return

	def read_command(self):
		'''
		@summary: read commands from command line, mainly input and output directory
		@str inputdir: input directory address, for P1 in/in.txt, for P2 opposite
		@str outputdir: outputdir directory address, for P2 out/out.txt, for P1 opposite
		'''
		if sys.argv[1] == '-s':
			inputdir = sys.argv[3]
			outputdir = sys.argv[5]
		else:
			inputdir = sys.argv[2]
			outputdir = sys.argv[4]
		return inputdir, outputdir
	
	def take_turn(self, str_player, inputdir, outputdir, b_first):
		'''
		@summary: Player's behavior in his turn
		@param str_player: indicates whose turn is going on, P1 represents first player
		@param inputdir, outputdir: input and output directory address
		@b_first: if it's the first turn, the player shouldn't pull board from file
		'''
		print str_player + '\'s Turn:'
		if not b_first:
			self.pull_board(inputdir)
			if sum(self.ls_board) == 0:
				print 'You ('+ str_player + ') lost!'
				os.remove(inputdir)
				exit()
			os.remove(inputdir)
		self.display_board()
		ls_move = self.nim(self.ls_board)
		file_output = open("move.txt", 'w')
		file_output.write("%s" % str(chr(ls_move[0]+65)+','+str(ls_move[1])))
		file_output.close()
		row   = self.get_row('move.txt')
		count = self.get_int('move.txt', 1, self.ls_board[row - 1])
		os.remove('move.txt')
		self.ls_board[row - 1] = self.ls_board[row - 1] - count
		self.push_board(outputdir)

	def nim(self, misere=True):
		''' strategy to create move, given current board create movement '''
		''' Ack: wiki '''
		heaps = self.ls_board
		count, not_empty_heap, i_not_empty = 0,0,0
		for i, heap in enumerate(heaps):
			if heap != 0:
				count += 1
				i_not_empty = i
		if count == 1:
			return [i_not_empty, heaps[i_not_empty]]
		X = reduce(lambda x,y: x^y, heaps)
		if X == 0: # Will lose unless all non-empty heaps have size one
			for i, heap in enumerate(heaps):
				if heap > 0: # Empty any (non-empty) heap
					chosen_heap, nb_remove = i, heap
					break
		else:
			sums = [t^X < t for t in heaps]
			chosen_heap = sums.index(True)
			nb_remove = heaps[chosen_heap] - (heaps[chosen_heap]^X)
			heaps_twomore = 0
			for i, heap in enumerate(heaps):
				n = heap-nb_remove if chosen_heap == i else heap
				if n>1: heaps_twomore += 1
			if heaps_twomore == 0:
				chosen_heap = heaps.index(max(heaps))
				heaps_one = sum(t==1 for t in heaps)
				nb_remove = heaps[chosen_heap]-1 if heaps_one%2!=misere else heaps[chosen_heap]
		print 'MOVE:', chr(chosen_heap+65), nb_remove
		return [chosen_heap, nb_remove]


	def create_move(self):
		''' given current board status, create movement '''
		Max = 0
		for i in range(len(self.ls_board)):
			if self.ls_board[i] > Max:
				Max = self.ls_board[i]
				maxIndex = i
		return [maxIndex,1]


	def get_row(self, inputdir):
		''' 
		@summary: get row number from inputdir
		@inputdir: here should be 'move.txt' which created from create_move
		@return: row number of this move
		'''
		answer = None
		while answer is None:
			try:
				file_input = open(inputdir, 'r')
			except IOError:
				time.sleep(5)
				continue
			row = ord(file_input.read().split(',')[0])-ord('A')+1
			file_input.close()
			# if taking a row which is empty, will ask to type in again
			if self.ls_board[row - 1] == 0:
				print 'That row is empty!'
			else:
				answer = row
		return answer
	
	def get_int(self, inputdir, min_value, max_value):
		'''
		@summary: get the number of sticks to take
		@inputdir: here should be 'move.txt' which created from create_move
		@min_value: the smallest value you can take away in this heap
		@max_value: the largest value you can take away in this heap
		'''
		answer = None
		while answer is None:
			try:
				file_input = open(inputdir, 'r')
			except IOError:
				time.sleep(5)
				continue
			response = file_input.read().split(',')[1]
			file_input.close()
			try:
				converted = int(response)
				if converted < min_value:
					print 'You lose.'
					exit()
				elif converted > max_value:
					print 'Number is too big.'
					exit()
				else:
					answer = converted
			except ValueError:
				print 'That is not a number!'
		return answer

	def pull_board(self, inputdir):
		'''
		@summary: update board from the other's file
		@param inputdir: for P1 the input is in/in.txt, for P2 is out/out.txt 
		'''
		while True:
			try:
				file_input = open(inputdir, 'r')
			except IOError:
				time.sleep(1)
				continue
			ls_in =  file_input.read().splitlines()
			for i in range(len(self.ls_board)):
				self.ls_board[i] = int(ls_in[i].split(' ')[1])
			file_input.close()
			return

	def push_board(self, outputdir):
		'''
		@summary: send board info to the other
		@outputdir: for P1 it's out/out.txt, for P1 is in/in.txt
		'''
		file_output = open(outputdir, 'w')
		for i in range(len(self.ls_board)-1):
			file_output.write("%s\n" % str(chr(65+i)+' '+str(self.ls_board[i])))
		file_output.write(str(chr(65+i+1)+' '+str(self.ls_board[i+1])))

	def display_board(self):
		'''
		@summary: show the current board information
		'''
		for i in range(0, len(self.ls_board), 1):
			print chr(ord('A')+i) + ': ' + ('*' * self.ls_board[i])


if __name__ == '__main__':
	''' test playing '''
	Coins().play()