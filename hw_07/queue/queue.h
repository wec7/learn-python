/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: implement a queue using a linked list
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include <iostream>
#include <vector>
#include <boost/random/exponential_distribution.hpp>
#include <boost/random/uniform_int_distribution.hpp>
#include <boost/random/mersenne_twister.hpp>
#include <boost/random/bernoulli_distribution.hpp>
using namespace std;

class queue
{
	/* data */
	int t;
	vector<pair<double, int>> path;
public:
	/* constructor */
	queue(int _time): t(_time){}
	/* methods */
	void monteCarlo_simulation(double, double);
	double avg_queue_len();
	int count_empty_queue();
};