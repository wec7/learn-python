/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: dynamic array of pointers to stings
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include "dynamic_array.h"

int main(int argc, char const *argv[])
{
	dynamic_array darray(100);

	cout << "1. Test for insert method: ";
	darray.insert(1, "d");
	darray.insert(2, "c");
	darray.insert(3, "b");
	darray.insert(4, "a");
	darray.print();

	cout << "2. Test for delete method: ";
	darray.remove(1);
	darray.print();

	cout << "3. Test for sort method: ";
	darray.sort();
	darray.print();
	return 0;
}