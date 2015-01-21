/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: dynamic array of pointers to stings
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#ifndef DYNAMICARRAY_H
#define DYNAMICARRAY_H

#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class dynamic_array
{
	/* data */
	int cur_size;
	int max_size;
	string** p_str;
public:
	dynamic_array(int n);
	~dynamic_array();

	/* methods */
	void remove(int);
	void insert(int, string);
	void print();
	void sort();
};

#endif