/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: single linked list lib
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include <iostream>
#include <string>
#include <list>
using namespace std;

class linked_list
{
	/* 
	@summary: Single linked lists 
	@param list: stl list
	@param head: iterator at head of the list
	*/
	list<string> list;
	std::list<string>::iterator head;
public:
	linked_list() {head = list.begin();}
	void Print();
	void Add(string given_name, string new_name);
	void Delete(string name);
	void Add(int n, string name);
	void Delete(int n);
	void Delete_next(int n);
	void rDelete(int n);
	void Add_back(string name);
	void Sort();
};

