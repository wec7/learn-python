/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: A stack using an STL Vector.
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include "vector_stack.h"

void vector_stack::push(int element){
	/* stack push */
	if (capacity == vec.capacity()) {
		capacity += 1;
		vec.push_back(element);
		return;
	}
	vec[capacity] = element;
	capacity++;
	return;
}

void vector_stack::pop() {
	/* stack pop */
	if (capacity == 0) {
		cout << "Error: Empty stack" << endl;
		return;
	}
	capacity -= 1;
}

void vector_stack::print(){
	/* stack elements print */
	for (int i = 0; i < capacity; ++i)
		cout << vec[i] << ' ';
	cout << endl;
}

int vector_stack::top(){
	/* return top element of the stack */
	return vec[capacity-1];
}