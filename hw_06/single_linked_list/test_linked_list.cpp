/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: test for linked list, same for double's and single's
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include "single_linked_list.h"
using namespace std;

int main(int argc, char const *argv[])
{
	linked_list slist;

	// 1. Test for function that adds a name after a given name. If no name is found, add the element at the end. 
	slist.Add("a", "a");
	slist.Add("a", "c");
	slist.Add("a", "b");
	cout << "1. Test for function that adds a name after a given name:" << endl;
	slist.Print();

	// 2. Test for function that deletes an element referenced by the name. If no name is found, do nothing.
	slist.Delete("a");
	slist.Delete("d");
	cout << "2. Test for function that deletes an element referenced by the name:" << endl;
	slist.Print();

	// 3. Test for the function that adds a name after the n-th element. If n> size of list, add at the end. 
	slist.Add(1, "a");
	slist.Add(100, "d");
	cout << "3. Test for the function that adds a name after the n-th element:" << endl;
	slist.Print();

	// 4. Test for the function to delete the n-th element in a single linked list. If n > size of the list, do nothing. 
	slist.Delete(3);
	slist.Delete(100);
	cout << "4. Test for the function to delete the n-th element in a single linked list:" << endl;
	slist.Print();

	// 5. Test for the function that deletes the name after the n-th element
	slist.Delete_next(2);
	cout << "5. Test for the function that deletes the name after the n-th element:" << endl;
	slist.Print();

	// 6. Test for the function that deletes the n-th element from the end of the list. 
	slist.rDelete(2);
	cout << "6. Test for the function that deletes the n-th element from the end of the list:" << endl;
	slist.Print();

	// 7. Test for the sort function
	slist.Add_back("Bob");
	slist.Add_back("Alice");
	slist.Add_back("john");
	slist.Sort();
	cout << "7. Test for the sort function:" << endl;
	slist.Print();

	return 0;
}