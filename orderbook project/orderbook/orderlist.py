"""
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: OrderList module modified from Python orderbook module
Modifier: Weiyi Chen
Ack: Michael Nguyen, orderbook module
"""

class OrderList(object):
    '''
    A doubly linked list of Orders. Used to iterate through Orders when
    a price match is found. Each OrderList is associated with a single
    price. Since a single price match can have more quantity than a single 
    Order, we may need multiple Orders to fullfill a transaction. The
    OrderList makes this easy to do. OrderList is naturally arranged by time.
    Orders at the front of the list have priority.
    '''

    def __init__(self):
        '''
        @summary: initialization
        @mem head_order: first order in the list
        @mem tail_order: last order in the list
        @mem length: number of Orders in the list
        @mem volume: sum of Order quantity in the list AKA share volume
        @mem last: helper for iterating 
        '''
        self.head_order = None 
        self.tail_order = None  
        self.length = 0 
        self.volume = 0  
        self.last = None  

    def __len__(self):
        ''' return length of the OrderList '''
        return self.length

    def __iter__(self):
        ''' iterator of the OrderList '''
        self.last = self.head_order
        return self

    def next(self):
        ''' get the next order in the list '''
        if self.last == None:
            raise StopIteration
        else:
            return_value = self.last
            self.last = self.last.next_order
            return return_value

    def get_head_order(self):
        ''' get the head_order in the list '''
        return self.head_order

    def append_order(self, order):
        ''' add order into the list '''
        if len(self) == 0:
            order.next_order = None
            order.prev_order = None
            self.head_order = order
            self.tail_order = order
        else:
            order.prev_order = self.tail_order
            order.next_order = None
            self.tail_order.next_order = order
            self.tail_order = order
        self.length +=1
        self.volume += order.quantity

    def remove_order(self, order):
        ''' 
        @summary: remove order from the list
        @details: remove an Order from the OrderList, first grab next / prev 
            order
        from the Order we are removing, then relink everything. Finally remove 
            the Order.
        '''
        self.volume -= order.quantity
        self.length -= 1
        if len(self) == 0: 
            return
        next_order = order.next_order
        prev_order = order.prev_order
        if next_order != None and prev_order != None:
            next_order.prev_order = prev_order
            prev_order.next_order = next_order
        elif next_order != None:
            next_order.prev_order = None
            self.head_order = next_order 
        elif prev_order != None: 
            prev_order.next_order = None
            self.tail_order = prev_order 

    def move_to_tail(self, order):
        ''' move order to the tail of the OrderList after updating '''
        if order.prev_order != None: #
            order.prev_order.next_order = order.next_order 
        else:
            self.head_order = order.next_order 

        order.next_order.prev_order = order.prev_order
        self.tail_order.next_order = order
        self.tail_order = order

    def __str__(self):
        ''' print OrderList info to debug '''
        from cStringIO import StringIO
        temp_file = StringIO()
        for order in self:
            temp_file.write("%s\n" % str(order))
        return temp_file.getvalue()
            

            

