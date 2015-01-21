/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: Implement a binary tree. Implement BFS and DFS algorithms to print.
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include <iostream>
#include <stack>
#include <queue>
using namespace std;

class TreeNode{
public:
	/* data */
	int val;
	TreeNode *left;
	TreeNode *right;
	/* constructor */
	TreeNode(int x): val(x), left(NULL), right(NULL) {}
};

void breadth_first_search(TreeNode* root);
void depth_first_search(TreeNode* root);