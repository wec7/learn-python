/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: dynamic array of pointers to stings
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include "dynamic_array.h"

dynamic_array::dynamic_array(int n) {
	/* constructor */
	p_str = new string*[n];
	cur_size = 0;
	max_size = n;
}

dynamic_array::~dynamic_array() {
	/* destructor */
	for(int i = 0; i < cur_size; i++) 
		delete p_str[i];
	delete [] p_str;
}

void dynamic_array::remove(int n_th) {
	/* deletion */
	if (n_th >= max_size)
		return;
	if (n_th < cur_size) {
		for(int i = n_th; i <= cur_size-1; i++)
			p_str[i-1] = p_str[i];
		cur_size--;
	}
	else if (n_th == cur_size) {
		p_str[n_th - 1] = NULL;
		cur_size--;
	}
}

void dynamic_array::insert(int n_th, string elem) {
	/* 
	@summary: Implement a similar function to insert the n-th element in the array. 
	@param n_th: the position
	@param elem: the inserted string
	*/
	if (n_th > max_size)
		return;
	if (n_th >= cur_size) {
		p_str[n_th - 1] = new string(elem);
		cur_size++;
	}
	else {
		for (int i = cur_size; i >= n_th; i--)
			p_str[i] = new string(*p_str[i-1]);
		p_str[n_th - 1] = new string(elem);
		cur_size++;
	}
}

void dynamic_array::print() {
	/* print the names in order following these operations. */
	for (int i = 0; i < cur_size; i++)
		cout << (*p_str[i]) << ' ';
	cout << endl;
}

void Merge(string* data[], int start, int mid, int end) {
	vector<string*> temp;
	int iter1 = start;
	int iter2 = mid + 1;
	while(iter1 <= mid && iter2 <= end) {
		if((*data[iter1]) <= (*data[iter2])) 
			temp.push_back(data[iter1++]);
		else 
			temp.push_back(data[iter2++]);
	}
	if(iter1 > mid && iter2 <= end)
		while(iter2 <= end) 
			temp.push_back(data[iter2++]);
	else if(iter2 > end && iter1 <= mid)
		while(iter1 <= mid) 
			temp.push_back(data[iter1++]);	
	for(int i = 0; i < (end - start + 1); i++) 
		data[start + i] = temp[i]; 
}

void MergeSort(string* data[], int start, int end) {
	if (end <= start)
		return;
	int middle = (start + end) / 2;
	MergeSort(data, start, middle);
	MergeSort(data, middle + 1, end);
	Merge(data, start, middle, end);
}

void dynamic_array::sort() {
	/* Implement a function to sort the array, by changing the pointers in the array */
	MergeSort(p_str, 0, cur_size-1);
}