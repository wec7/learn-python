/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: Tests for BFS and DFS on binary tree
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include "binary_tree.h"

int main(int argc, char const *argv[])
{
	// Tree construction
	TreeNode *root;
	root = new TreeNode(1);
	root->left = new TreeNode(2);
	root->right = new TreeNode(3);
	root->left->left = new TreeNode(4);
	root->left->right = new TreeNode(5);
	root->right->left = new TreeNode(6);
	root->right->right = new TreeNode(7);
	
	// The breadth-first search algorithm to print nodes in order
	cout << "The breadth-first search algorithm to print nodes in level order:" << endl;
	breadth_first_search(root);

	// The depth-first search algorithm to print nodes in order
	cout << "TThe depth-first search algorithm to print nodes in order:" << endl;
	depth_first_search(root);
	return 0;
}