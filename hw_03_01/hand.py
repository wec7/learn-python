"""
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: Hand module to descible poker hand
Author: Weiyi Chen, Yun Peng
Acknowledge: python-poker-engine
"""

# My own module import
from card import *

# Global variables
HIGHCARD, PAIR, TWOPAIR, SET, STRAIGHT, \
FLUSH, FULLHOUSE, QUADS, STRAIGHTFLUSH = range(9)
TYPE_NAMES = {
    HIGHCARD:      'HIGHCARD',
    PAIR:          'PAIR',
    TWOPAIR:       'TWOPAIR',
    SET:           'SET',
    STRAIGHT:      'STRAIGHT',
    FLUSH:         'FLUSH',
    FULLHOUSE:     'FULLHOUSE',
    QUADS:         'QUADS',
    STRAIGHTFLUSH: 'STRAIGHTFLUSH'
}


class Hand(object):
    '''
       A set of cards with support for determining which poker hand
       the cards form.  Also supports comparing two hands for determining
       who 'wins' in a showdown. Note that the analysis performed searches
       for the *best* possible poker hand.  
    '''

    def __init__(self):
        self.cards = []
        self.dirty = False
        self.type = HIGHCARD
        self.ranks = []

    @classmethod
    def from_str(cls, s):
        '''Creates a hand from a string like Ad Th 3s 5c 7d '''
        parts = [Card.from_str(part) for part in s.split()]
        h = Hand()
        for c in parts: h.add(c)
        h.dirty = True
        return h

    def add(self, card):
        '''adds a card to the hand. avoid accessing the cards directly'''
        self.cards.append(card)
        self.dirty = True

    def get_type(self):
        '''returns one of HIGHCARD, PAIR, etc. and requires 5 cards in the hand'''
        if not self.dirty: return self.type
        self._analyze()
        return self.type

    def describe(self):
        '''returns description of hand such as 'ace-high' or 'pair of tens'
           when long_fmt is True (default) or an abbreviated string 
           representation of the hand's cards as in 'Ad Th 3s 5c 7d 8d Qc'
           when long_fmt is False'''
        if self.dirty: self._analyze()
        return ' '.join([str(c) for c in self.cards])

    def __str__(self):
        '''same as describe()'''
        return self.describe()

    def __cmp__(self, other):
        '''compare hands following standard poker hand rankings, 
           including kickers.'''
        type = self.get_type()
        other_type = other.get_type()
        n = cmp(type, other_type)
        if n != 0: return n
        if self.ranks == other.ranks: return 0
        if self.ranks < other.ranks: return -1
        return 1

    def _analyze(self):
        '''determine the best hand possible given the current set of cards'''
        self.dirty = False
        if len(self.cards) < 5: return
        r2c = {}
        s2c = {}
        for c in self.cards: r2c.setdefault(c.rank, []).append(c)
        for c in self.cards: s2c.setdefault(c.suit, []).append(c)
        for r in r2c: 
            r2c[r].sort()
            r2c[r].reverse()
        for s in s2c: 
            s2c[s].sort()
            s2c[s].reverse()
        self._find_straightflush(r2c,s2c) or \
        self._find_quads(r2c,s2c) or \
        self._find_fullhouse(r2c,s2c) or \
        self._find_flush(r2c,s2c) or \
        self._find_straight(r2c,s2c) or \
        self._find_set(r2c,s2c) or \
        self._find_twopair(r2c,s2c) or \
        self._find_pair(r2c,s2c) or \
        self._find_highcard(r2c,s2c)
        return r2c, s2c

    def _largest_rank_with_n(self, r2c, n, ignore0 = -1, ignore1 = -1):
        '''return the largest rank such that n cards have the rank.'''
        for r in range(ACE, TWO-1, -1):
            if r != ignore0 and r != ignore1 and len(r2c.get(r, [])) == n: 
                return r
        return -1

    def _kickers(self, n, ignore0 = -1, ignore1 = -1):
        '''find n 'kicker' cards that do not have rank ignore1 nor ignore2.'''
        ranks = [c.rank for c in self.cards if c.rank != ignore0 and 
                                               c.rank != ignore1]
        ranks.sort()
        ranks.reverse()
        return ranks[0:n]

    def _find_straightflush(self, r2c, s2c): 
        if not self._find_straight(r2c,s2c): return False
        tally = [0,0,0,0]
        for s in range(4):
            for r in self.ranks:
                if len([c for c in r2c[r] if c.suit == s]) > 0:
                    tally[s] += 1
            if tally[s] >= 5:
                self.type = STRAIGHTFLUSH
                return True
        return False

    def _find_quads(self, r2c, s2c): 
        r = self._largest_rank_with_n(r2c, 4)
        if r == -1: return False
        self.type = QUADS
        self.ranks = [r,r,r,r] + self._kickers(1, r)
        return True

    def _find_fullhouse(self, r2c, s2c): 
        trip_rank = self._largest_rank_with_n(r2c, 3)
        if trip_rank == -1: return False
        pair_rank = self._largest_rank_with_n(r2c, 2, trip_rank)
        if pair_rank == -1: return False
        self.type = FULLHOUSE
        self.ranks = [trip_rank, trip_rank, trip_rank, pair_rank, pair_rank]
        return True

    def _find_flush(self, r2c, s2c): 
        for s in range(4):
            if len(s2c.get(s,[])) >= 5:
                self.type = FLUSH
                self.ranks = [c.rank for c in s2c[s][0:5]]
                return True
        return False

    def _find_straight(self, r2c, s2c):
        r, n = ACE, 0
        while r >= TWO:
            if len(r2c.get(r, [])) > 0:
                n = n + 1
                if n == 5: break
            else:
                n = 0
            r = r - 1
        found = False
        if n == 5:
            found = True
            self.ranks = range(r + n - 1, r - 1, -1)
        elif n == 4 and r < TWO and len(r2c.get(ACE, [])) > 0:
            self.ranks = [FIVE, FOUR, THREE, TWO, ACE]
            found = True
        if found:
            self.type = STRAIGHT
        return found

    def _find_set(self, r2c, s2c): 
        r = self._largest_rank_with_n(r2c, 3)
        if r == -1: return False
        self.type = SET
        self.ranks = [r,r,r] + self._kickers(2, r)
        return True

    def _find_twopair(self, r2c, s2c): 
        r0 = self._largest_rank_with_n(r2c, 2)
        if r0 == -1: return False
        r1 = self._largest_rank_with_n(r2c, 2, r0)
        if r1 == -1: return False
        self.type = TWOPAIR
        min_r, max_r = (min(r0,r1), max(r0,r1))
        self.ranks = [max_r, max_r, min_r, min_r] + self._kickers(1, r0, r1)
        return True

    def _find_pair(self, r2c, s2c): 
        r = self._largest_rank_with_n(r2c, 2)
        if r == -1: return False
        self.type = PAIR
        self.ranks = [r,r] + self._kickers(3, r)
        return True

    def _find_highcard(self, r2c, s2c):
        self.type = HIGHCARD
        self.ranks = self._kickers(5)
        return True
