/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: A stack using an STL Vector
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include <list>
#include <iostream>
using namespace std;

class singlylist_stack
{
	/* data */
	list<int> ls;
public:
	/* methods */
	void pop();
	void push(int element);
	void print();
	int top();	
};