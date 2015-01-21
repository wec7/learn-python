/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: A stack using an STL List.
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include "singlylist_stack.h"

void singlylist_stack::push(int element) {
	/* stack push */
	ls.push_back(element);
	return;
}

void singlylist_stack::pop() {
	/* stack pop */
	ls.pop_back();
	return;
}

void singlylist_stack::print() {
	/* stack elements print */
	for(list<int>::const_iterator it = ls.begin(); it != ls.end(); it++)
		cout << *it << ' ';
	cout << endl;
}

int singlylist_stack::top() {
	/* return top element of the stack */
	return ls.back();
}