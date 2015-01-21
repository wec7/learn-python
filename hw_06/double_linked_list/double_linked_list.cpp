/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: double linked list implementation
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include "double_linked_list.h"

void linked_list::Print() {
	/* Print the contents of the list */
	cout << "\t";
	for (std::list<string>::iterator it=list.begin(); it!=list.end(); it++) {
		if (it != list.begin())
			cout << " --> " << *it;
		else 
			cout << *it;
	}
		
	cout << " --> NULL" << endl;
}

void linked_list::Add(string given_name, string new_name) {
	/*  
	@summary: adds a name after a given name
	if no name is found, add the element at the end. 
	*/
	bool found = false;
	for (std::list<string>::iterator it=list.begin(); it!=list.end(); it++)
		if (*it == given_name) {
			list.insert(++it,new_name);
			found = true;
			break;
		}
	if (found == false)
		list.push_back(new_name);
}

void linked_list::Delete(string name) {
	/*
	@summary: deletes an element referenced by the name. If no name is found, do nothing.
	@param name: the name of the delete node
	*/
	list.remove(name);
}

void linked_list::Add(int n, string name) {
	/* adds a name after the n-th element, n is base 1 */
	if (n > list.size()) {
		list.push_back(name);
		return;
	}
	std::list<string>::iterator it=list.begin();
	for (int i = 1; i < n; i++)
		it++;
	list.insert(it, name);
}

void linked_list::Delete(int n) {
	/* delete the n-th element in a single linked list, n is base 1 */
	if (n > list.size())
		return;
	std::list<string>::iterator it=list.begin();
	for (int i = 1; i < n; i++)
		it++;
	list.remove(*it);
}

void linked_list::Delete_next(int n) {
	/* create a function that deletes the name after the n-th element */
	Delete(n+1);
}

void linked_list::rDelete(int n) {
	/* create a function that deletes the n-th element from the end of the list */
	if (n > list.size())
		return;
	std::list<string>::iterator it=list.end();
	for (int i = 1; i <= n; i++)
		it--;
	list.remove(*it);
}

void linked_list::Add_back(string name) {
	/* add methods to add elements at the back of the list */
	list.push_back(name);
}

void linked_list::Sort() {
	/* Create a function that takes a single linked list and sorts the elements by name alphabetically */
	list.sort();
}
