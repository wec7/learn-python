"""
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: Ordertree module modified from Python orderbook module
Modifier: Weiyi Chen
Ack: Michael Nguyen, orderbook module
"""

# Orderbook imports
from bintrees import RBTree
from orderlist import OrderList
from order import Order

class OrderTree(object):
    ''' An RBtree used to store OrderLists in price order '''

    def __init__(self):
        '''
        @summary: initialization of Ordertree class
        @mem price_tree: a red-black tree
        @mem price_map: Dictionary containing price : OrderList object
        @mem order_map: Dictionary containing order_id : Order object
        @mem volume: Contains total quantity from all Orders in tree
        @mem num_orders: Contains count of Orders in tree
        @mem depth: Number of different prices in tree (http://en.wikipedia.org/wiki/Order_book_(trading)#Book_depth)
        '''
        self.price_tree = RBTree()
        self.price_map = {} 
        self.order_map = {} 
        self.volume = 0
        self.num_orders = 0 
        self.depth = 0 

    def __len__(self):
        ''' return the length of order_map '''
        return len(self.order_map)

    def get_price_list(self, price):
        ''' get the price list from the price map '''
        return self.price_map[price]

    def get_order(self, order_id):
        ''' get order list from order map '''
        return self.order_map[order_id]

    def create_price(self, price):
        ''' create a new price if adding an order without price in the tree '''
        self.depth += 1
        new_list = OrderList()
        self.price_tree.insert(price, new_list) 
        self.price_map[price] = new_list 

    def remove_price(self, price):
        ''' remove a price from the tree '''
        self.depth -= 1 
        self.price_tree.remove(price)
        del self.price_map[price]

    def price_exists(self, price):
        ''' check whether price exists in price map '''
        return price in self.price_map

    def order_exists(self, order):
        ''' check whether an order exists in order map '''
        return order in self.order_map

    def insert_order(self, quote):
        ''' insert an order into the order map '''
        if self.order_exists(quote['order_id']):
            self.remove_order_by_id(quote['order_id'])
        self.num_orders += 1
        if quote['price'] not in self.price_map:
            self.create_price(quote['price']) # If price not in Price Map, create a node in RBtree
        order = Order(quote, self.price_map[quote['price']]) # Create an order
        self.price_map[order.price].append_order(order) # Add the order to the OrderList in Price Map
        self.order_map[order.order_id] = order
        self.volume += order.quantity

    def remove_order_by_id(self, order_id):
        ''' remove an order from the order map '''
        self.num_orders -= 1
        order = self.order_map[order_id]
        self.volume -= order.quantity
        order.order_list.remove_order(order)
        if len(order.order_list) == 0:
            self.remove_price(order.price)
        del self.order_map[order_id]

    def max_price(self):
        ''' return max price in price tree '''
        if self.depth > 0:
            return self.price_tree.max_key()
        else:
            return None

    def min_price(self):
        ''' return min price in price tree '''
        if self.depth > 0:
            return self.price_tree.min_key()
        else:
            return None

    def max_price_list(self):
        ''' return max price in price tree '''
        if self.depth > 0:
            return self.get_price_list(self.max_price())
        else:
            return None

    def min_price_list(self):
        ''' return min price in price tree '''
        if self.depth > 0:
            return self.get_price_list(self.min_price())
        else:
            return None
