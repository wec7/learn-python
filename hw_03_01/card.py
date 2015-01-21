"""
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: Card module to descible poker hand
Author: Weiyi Chen, Yun Peng
"""

# Global variables
TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE = range(13)
DIAMONDS, HEARTS, CLUBS, SPADES = range(4)
RANK_ABBR = '23456789TJQKA'
SUIT_ABBR = 'dhcs'

class Card(object):
    '''A playing card; e.g. ace of hearts'''

    def __init__(self, val): 
        '''
           val is a value in [0,52) where [0,12] represents the 2-A ranks
           in the diamonds suit, [13,25] hearts, [26-38] clubs, and [39,51]
           spades.
        '''
        self.suit = val / 13
        self.rank = val % 13

    def __cmp__(self, other): 
        '''Cards are compared by their rank alone'''
        return cmp(self.rank, other.rank)

    def __str__(self): 
        '''Essentially describe'''
        return RANK_ABBR[self.rank] + SUIT_ABBR[self.suit]

    @classmethod
    def from_str(cls, s):
        '''return Card instance from a short format string representation 
           of the card such as Ac or 3D'''
        s = s.strip()
        if len(s) < 2:
            raise NameError("need string with two characters")
        rank, suit = s[0], s[1]
        if   rank >= '2' and rank <= '9': rank = int(rank)-2
        elif rank == 'A': rank = ACE
        elif rank == 'T': rank = TEN
        elif rank == 'J': rank = JACK
        elif rank == 'Q': rank = QUEEN
        elif rank == 'K': rank = KING
        else: raise NameError("unknown card rank '%s'" % rank)
        if   suit == 's' or 'S': suit = SPADES
        elif suit == 'c' or 'C': suit = CLUBS
        elif suit == 'd' or 'D': suit = DIAMONDS
        elif suit == 'h' or 'H': suit = HEARTS
        else: raise NameError("unknown card suit '%s'" % suit)
        return Card(suit * 13 + rank)