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
Usage: python final2.py
Author: Weiyi Chen
Ack: Michael Nguyen, orderbook module
"""
# Python imports
import argparse

# 3rd party imports
from orderbook import OrderBook

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


def print_orderBook(order_book, trades=None, out_file='output.txt'):
	'''
	@summary: print the output as the question required
	@details: Write to the output a stream of quotes and trades that the 
		incoming messages generate. For every trade write TRADE followed after 
		space by the trade size and price. For every quote write QUOTE followed 
		after space by the quote bid size, bid price, minus sign (``-"), ask 
		size, ask price (all separated by spaces).
	@param order_book: an orderbook containing all the order information
	@param trades: if trades is not none, will print trades first
	@return: None
	'''
	if trades:
		for trade in trades:
			print 'TRADE', int(trade['quantity']), int(trade['price'])
			out_file.write('TRADE '+str(int(trade['quantity']))+' '+str(int(trade['price']))+'\n')
	best_bid = order_book.get_best_bid()
	best_bid_volume = int(order_book.get_volume_at_price('bid',best_bid))
	best_ask = order_book.get_best_ask()
	best_ask_volume = int(order_book.get_volume_at_price('ask',best_ask))
	print 'QUOTE', best_bid_volume, 
	out_file.write('QUOTE '+str(best_bid_volume)+' ')
	if best_bid:
		print int(best_bid),
		out_file.write(str(int(best_bid))+' ')
	else:
		print 0,
		out_file.write('0 ')
	print '-', best_ask_volume,
	out_file.write('- '+str(best_ask_volume)+' ')
	if best_ask:
		print int(best_ask)
		out_file.write(str(int(best_ask))+'\n')
	else:
		print 99999
		out_file.write('99999\n')

def rm_order(order_book, ls_splitCmd, out_file):
	''' 
	@summary: cancel orders from the order_book
	@details: CANCEL denotes a request to cancel previously issued order. It 
		is followed by a single integer i which is the number of the message 
		with some preceding order to buy or to sell (messages are numbered 
		from 1 to n).
	@param order_book: an orderbook containing all the order information,
		this is where the order canceled from
	@param ls_splitCmd: splited commands from input, with syntex as [CANCEL, 
		Command_Num]
	@return: None, but will print out new best bid and best ask with volumes
	'''
	order_book.cancel_order('ask', order_id=int(ls_splitCmd[1])-1)
	order_book.cancel_order('bid', order_id=int(ls_splitCmd[1])-1)
	print_orderBook(order_book, out_file=out_file)

def add_order(order_book, ls_splitCmd, i_orderID, out_file):
	'''
	@summary: add orders to the order_book
	@details: If an order to buy arrives to the order book at a price greater 
		or equal to the current ask price, then the corresponding orders are 
		matched and trade happens -- buyer and seller reached agreement on a 
		price. Vice versa, if an order to sell arrives to the order book at a 
		price less or equal to the current bid price, then trade happens, too. 
	@param order_book: an orderbook containing all the order information,
		this is where the order added to
	@param i_orderID: the index of current command line used to label order
	@return: none, but will print out new best bid and best ask with volumes
	'''
	d_order =  {'type':'limit',
				'quantity':int(ls_splitCmd[1]),
				'price':int(ls_splitCmd[2]),
				#'trade_id':100,
				'order_id':i_orderID}
	if ls_splitCmd[0] == 'BUY':
		d_order['side'] = 'bid'
	else:
		d_order['side'] = 'ask'
	trades, order_id = order_book.process_order(d_order)
	print_orderBook(order_book, trades, out_file)

def solve_one_case(i_cmdNum, in_file, out_file):
	'''
	@summary: For each test case, the output must follow the description 
		The outputs of two consecutive cases will be separated by a blank line.
	@param i_cmdNum: the number of commands in this case
	@param in_file: input file containing the commands
	@return: none, this is the structure of solving one case
	'''
	order_book = OrderBook()
	for i in range(i_cmdNum):
		ls_splitCmd = in_file.readline().split()
		if ls_splitCmd[0] == 'BUY' or ls_splitCmd[0] == 'SELL':
			add_order(order_book, ls_splitCmd, i, out_file)
		elif ls_splitCmd[0] == 'CANCEL':
			rm_order(order_book, ls_splitCmd, out_file)
		else:
			raise IOError

def main():
	''' main file to read in inputs and solve each case one by one '''
	in_file = open(read_arg().i,'r')
	out_file = open(read_arg().o,'w')
	while True:
		str_line = in_file.readline()
		if str_line:
			solve_one_case(int(str_line), in_file, out_file)
			print 
			out_file.write('\n')
		else:
			break

if __name__ == '__main__':
	main()