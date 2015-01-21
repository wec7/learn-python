/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: Implement the breadth-first search and depth first search algorithms and print the nodes in order.
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include "binary_tree.h"

void breadth_first_search(TreeNode* root){
	/* The breadth-first search algorithm to print nodes in level order */
	queue<TreeNode*> q_tree;
	q_tree.push(root);
	while (!q_tree.empty()) {
		TreeNode *node = q_tree.front();
		q_tree.pop();
		cout << node->val << ' ';
		if (node->left != NULL) 
			q_tree.push(node->left);
		if (node->right != NULL) 
			q_tree.push(node->right);
	}
	cout << endl;
	return;
}

void depth_first_search(TreeNode *root){
	/* The depth-first search algorithm to print nodes in order */
	stack<TreeNode*> s_tree;
	while (!s_tree.empty() || root != NULL) {
		if (root != NULL) {
			s_tree.push(root);
			root = root->left;
		}
		else {
			root = s_tree.top();
			s_tree.pop();
			cout << root->val << ' ';
			root = root->right;
		}
	}
	cout << endl;
	return;
}