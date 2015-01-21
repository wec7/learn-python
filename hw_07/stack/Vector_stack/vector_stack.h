/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: A stack using an STL Vector
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include <vector>
#include <iostream>
using namespace std;

class vector_stack
{
	/* data */
	vector<int> vec;
	int capacity;
	
public:
	vector_stack(): capacity(0){};

	/* methods */
	void pop();
	void push(int m);
	void print();
	int top();
};