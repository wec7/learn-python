/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: the Hanoi tower problem using vector stack to solve
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include "vector_stack.h"

void Move(int n, vector_stack *stacks, int stack_from, int stack_to, int stack_extra){
	/* Recursion to solve Hanoi tower problem, print all the steps necessary to solve the problem */
	if (n == 0)
		return;
	Move(n-1, stacks, stack_from, stack_extra, stack_to);
	int temp = stacks[stack_from-1].top();
	stacks[stack_to-1].push(temp);
	stacks[stack_from-1].pop();
	cout << "Move element " << temp << " from stack " << stack_from << " to stack "<< stack_to << endl;
	Move(n-1, stacks, stack_extra, stack_to, stack_from);
}

void HanoiTower(int n){
	/* the Hanoi tower problem using stacks */
	vector_stack stacks[3];
	for (int i = n; i > 0; i--)
		stacks[0].push(i);
	Move(n, stacks, 1, 3, 2);
}

int main(int argc, char const *argv[])
{
	/* require 2^n-1 steps to move n elements from stack 1 to stack 3 */
	HanoiTower(3);
	return 0;
}