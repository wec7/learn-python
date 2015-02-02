"""
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: Orderbook module modified from Python orderbook module
Modifier: Weiyi Chen
Ack: Michael Nguyen, orderbook module
"""
# Python imports
import sys
import math
from collections import deque # a faster insert/pop queue
from cStringIO import StringIO

# Orderbook import
from ordertree import OrderTree

class OrderBook(object):
    ''' Orderbook utilizing all the other modules '''
    def __init__(self):
        '''
        @summary: initialization of OrderBook
        @mem bids: an ordertree for bids orders
        @mem asks: an ordertree for asks orders
        @mem time: maintain the current time in the orderbook
        '''
        self.bids = OrderTree()
        self.asks = OrderTree()
        self.last_timestamp = 0
        self.time = 0
        self.next_order_id = 0

    def update_time(self):
        ''' update time automatically '''
        self.time += 1

    def process_order(self, quote):
        '''
        @summary: add order given quote
        @quote: a dictionary containing order information
        @return trades: return trades if there exists for the order added
        @return order_in_book: containing all orders in orderbook
        '''
        order_type = quote['type']
        order_in_book = None
        self.update_time()
        quote['timestamp'] = self.time
        if quote['quantity'] <= 0:
            sys.exit('process_order() given order of quantity <= 0')
        self.next_order_id += 1
        trades, order_in_book = self.process_limit_order(quote)
        return trades, order_in_book

    def process_order_list(self, side, order_list, quantity_still_to_trade, quote):
        '''
        Takes an OrderList (stack of orders at one price) and an incoming order and matches
        appropriate trades given the order's quantity.
        '''
        trades = []
        quantity_to_trade = quantity_still_to_trade
        while len(order_list) > 0 and quantity_to_trade > 0:
            head_order = order_list.get_head_order()
            traded_price = head_order.price
            #counter_party = head_order.trade_id
            if quantity_to_trade < head_order.quantity:
                traded_quantity = quantity_to_trade
                # Do the transaction
                new_book_quantity = head_order.quantity - quantity_to_trade
                head_order.update_quantity(new_book_quantity, head_order.timestamp)
                quantity_to_trade = 0
            elif quantity_to_trade == head_order.quantity:
                traded_quantity = quantity_to_trade
                if side == 'bid':
                    self.bids.remove_order_by_id(head_order.order_id)
                else:
                    self.asks.remove_order_by_id(head_order.order_id)
                quantity_to_trade = 0
            else: # quantity to trade is larger than the head order
                traded_quantity = head_order.quantity
                if side == 'bid':
                    self.bids.remove_order_by_id(head_order.order_id)
                else:
                    self.asks.remove_order_by_id(head_order.order_id)
                quantity_to_trade -= traded_quantity
            transaction_record = {
                    'timestamp': self.time,
                    'price': traded_price,
                    'quantity': traded_quantity,
                    'time': self.time
                    }

            if side == 'bid':
                transaction_record['party1'] = ['bid', head_order.order_id]
                transaction_record['party2'] = ['ask', None]
            else:
                transaction_record['party1'] = ['ask', head_order.order_id]
                transaction_record['party2'] = ['bid', None]

            trades.append(transaction_record)
        return quantity_to_trade, trades

    def process_limit_order(self, quote):
        ''' 
        @summary: process limit order given quote as the new order 
        @param: a dictionary containing order infos
        @return trades: if causing any trade opportunites
        @return order_in_book: remaining orders in the orderBook
        '''
        order_in_book = None
        trades = []
        quantity_to_trade = quote['quantity']
        side = quote['side']
        price = quote['price']
        if side == 'bid':
            while (self.asks and price > self.asks.min_price() and quantity_to_trade > 0):
                best_price_asks = self.asks.min_price_list()
                quantity_to_trade, new_trades = self.process_order_list('ask', best_price_asks, quantity_to_trade, quote)
                trades += new_trades
            # If volume remains, need to update the book with new quantity
            if quantity_to_trade > 0:
                quote['order_id'] = self.next_order_id
                quote['quantity'] = quantity_to_trade
                self.bids.insert_order(quote)
                order_in_book = quote
        elif side == 'ask':
            while (self.bids and price < self.bids.max_price() and quantity_to_trade > 0):
                best_price_bids = self.bids.max_price_list()
                quantity_to_trade, new_trades = self.process_order_list('bid', best_price_bids, quantity_to_trade, quote)
                trades += new_trades
            # If volume remains, need to update the book with new quantity
            if quantity_to_trade > 0:
                quote['order_id'] = self.next_order_id
                quote['quantity'] = quantity_to_trade
                self.asks.insert_order(quote)
                order_in_book = quote
        else:
            sys.exit('process_limit_order() given neither "bid" nor "ask"')
        return trades, order_in_book

    def cancel_order(self, side, order_id, time=None):
        ''' 
        @summary: cancel order by order_id
        @param side: bid or ask
        @param order_id: id of such order
        '''
        if time:
            self.time = time
        else:
            self.update_time()
        if side == 'bid':
            if self.bids.order_exists(order_id):
                self.bids.remove_order_by_id(order_id)
        elif side == 'ask':
            if self.asks.order_exists(order_id):
                self.asks.remove_order_by_id(order_id)
        else:
            sys.exit('cancel_order() given neither "bid" nor "ask"')

    def get_volume_at_price(self, side, price):
        ''' 
        @summary: get the volume at some price
        @param side: bid or ask, choose which side to get that volume
        @param price: the price specified to get its volume
        @return: the volume
        '''
        if side == 'bid':
            volume = 0
            if self.bids.price_exists(price):
                volume = self.bids.get_price_list(price).volume
            return volume
        elif side == 'ask':
            volume = 0
            if self.asks.price_exists(price):
                volume = self.asks.get_price_list(price).volume
            return volume
        else:
            sys.exit('get_volume_at_price() given neither "bid" nor "ask"')

    def get_best_bid(self):
        ''' return best bid price in the orderbook '''
        return self.bids.max_price()

    def get_best_ask(self):
        ''' return best ask price in the orderbook '''
        return self.asks.min_price()


