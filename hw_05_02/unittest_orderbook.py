"""
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: unittest to test orderbook class
Usage: python unittest_orderbook.py
Author: Weiyi Chen
"""

# Python import
import unittest

# My own module import
from orderbook import OrderBook

class OrderBookTestCase(unittest.TestCase):
    ''' Unittest for the OrderBook module '''
    def setUp(self):
        self.order_book = OrderBook()
        self.limit_orders = [{'type' : 'limit', 
                   'side' : 'ask', 
                    'quantity' : 5, 
                    'price' : 101},
                   {'type' : 'limit', 
                    'side' : 'ask', 
                    'quantity' : 5, 
                    'price' : 103},
                   {'type' : 'limit', 
                    'side' : 'ask', 
                    'quantity' : 5, 
                    'price' : 101},
                   {'type' : 'limit', 
                    'side' : 'ask', 
                    'quantity' : 5, 
                    'price' : 101},
                   {'type' : 'limit', 
                    'side' : 'bid', 
                    'quantity' : 5, 
                    'price' : 99},
                   {'type' : 'limit', 
                    'side' : 'bid', 
                    'quantity' : 5, 
                    'price' : 98},
                   {'type' : 'limit', 
                    'side' : 'bid', 
                    'quantity' : 5, 
                    'price' : 99},
                   {'type' : 'limit', 
                    'side' : 'bid', 
                    'quantity' : 5, 
                    'price' : 97},
                   ]
        for order in self.limit_orders:
            trades, order_id = self.order_book.process_order(order)

    def test_process_asks_order(self):
        ''' set up asks orders for unittests '''
        self.assertEquals(self.order_book.asks.order_map[1].price, 101.0)
        self.assertEquals(self.order_book.asks.order_map[2].price, 103.0)
        self.assertEquals(self.order_book.asks.order_map[3].price, 101.0)
        self.assertEquals(self.order_book.asks.order_map[4].price, 101.0)

    def test_process_bids_order(self):
        ''' set up bids orders for unittests '''
        self.assertEquals(self.order_book.bids.order_map[5].price, 99.0)
        self.assertEquals(self.order_book.bids.order_map[6].price, 98.0)
        self.assertEquals(self.order_book.bids.order_map[7].price, 99.0)
        self.assertEquals(self.order_book.bids.order_map[8].price, 97.0)

    def test_trades(self):
        ''' Submitting a limit order that crosses the opposing best price 
        will result in a trade '''
        crossing_limit_order = {'type': 'limit',
                                'side': 'bid',
                                'quantity': 2,
                                'price': 102}
        trades, order_in_book = self.order_book.process_order(\
            crossing_limit_order)
        self.assertEquals(trades[0]['price'], 101)
        self.assertEquals(trades[0]['quantity'],2)

    def test_large_trades(self):
        ''' If a limit crosses but is only partially matched, the remaning 
        volume will be placed in the book as an outstanding order '''
        big_crossing_limit_order = {'type': 'limit',
                                    'side': 'bid',
                                    'quantity': 50,
                                    'price': 102}
        trades, order_in_book = self.order_book.process_order(\
            big_crossing_limit_order)
        self.assertEquals(order_in_book['price'], 102) 
        self.assertEquals(order_in_book['quantity'], 35)

if __name__ == '__main__':
    unittest.main() # Run unittest
