"""
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: Order module modified from Python orderbook module
Modifier: Weiyi Chen
Ack: Michael Nguyen, orderbook module
"""
# Python imports
import time, random

class Order(object):
    '''
    Orders represent the core piece of the exchange. Every bid/ask is an Order.
    Orders are doubly linked and have helper functions (next_order, prev_order)
    to help the exchange fullfill orders with quantities larger than a single
    existing Order.
    '''
    def __init__(self, quote, order_list):
        '''
        @summary: initialization of Order class
        @mem timestamp: integer representing the timestamp of order creation
        @mem quantity: decimal representing amount of thing - can be partial 
            amounts
        @mem price: decimal representing price (currency)
        @mem order_list: doubly linked list to make it easier to re-order 
            Orders for a particular price point
        '''
        self.timestamp = int(quote['timestamp']) # 
        self.quantity = float(quote['quantity']) # 
        self.price = float(quote['price']) # 
        self.order_id = int(quote['order_id'])
        self.next_order = None
        self.prev_order = None
        self.order_list = order_list

    def next_order(self):
        ''' helper functions to get next order in linked list '''
        return self.next_order

    def prev_order(self):
        ''' helper functions to get previous order in linked list '''
        return self.prev_order

    def update_quantity(self, new_quantity, new_timestamp):
        ''' 
        @summary: update order quantity according to given infos
        @param new_quantity: the order quantity need to changed be
        @param new_timestamp: the time when the order is changed
        '''
        if new_quantity > self.quantity and self.order_list.tail_order != self:
            # check to see that the order is not the last order in list and the quantity is more
            self.order_list.move_to_tail(self) # move to the end
        self.order_list.volume -= (self.quantity - new_quantity) # update volume
        self.timestamp = new_timestamp
        self.quantity = new_quantity

    def __str__(self):
        ''' print out order information to help debug '''
        return "Order: Price - %s, Quantity - %s, Order ID - %s" % (self.price,
            self.quantity, self.order_id)
