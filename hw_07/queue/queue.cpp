/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: implement a queue using a linked list
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include "queue.h"

void queue::monteCarlo_simulation(double arrivalLambda, double departureLambda){
	/* 
	@summary: a monte Carlo Simulation to simulate a Queue at a supermarket 
	@param arrivalLambda: a parameter for a Poisson distribution for the arrival with lambda
	@param departureLambda: a parameter for a Poisson distribution for the departure with lambda
	*/
	double cur_time = 0, cur_length = 0, waiting_time = 0;
	boost::random::mt19937 gen; // produces randomness
	boost::random::exponential_distribution<double> rand_exp_arrival(arrivalLambda);
	boost::random::exponential_distribution<double> rand_exp_arrival_departure(arrivalLambda + departureLambda);
	boost::random::bernoulli_distribution<double> rand_bernoulli(arrivalLambda / (arrivalLambda+departureLambda));
	path.push_back(make_pair(cur_time, cur_length));
	while (true) {
		if (cur_length == 0) {
			waiting_time = rand_exp_arrival(gen);
			cur_time += waiting_time;
			if (cur_time>t) {
				path.push_back(make_pair(t, cur_length));
				break;
			}
			cur_length = 1;
			path.push_back(make_pair(cur_time, cur_length));
		}
		else {
			waiting_time = rand_exp_arrival_departure(gen);
			cur_time += waiting_time;
			if (cur_time>t) {
				path.push_back(make_pair(t, cur_length));
				break;
			}
			if (rand_bernoulli(gen))
				cur_length += 1;
			else 
				cur_length -= 1;
			path.push_back(make_pair(cur_time, cur_length));
		}
	}
}

double queue::avg_queue_len(){
	/* calculate the average queue length */
	double length = 0;
	vector<pair<double, int>>::const_iterator it_cur = path.begin();
	vector<pair<double, int>>::const_iterator it_next = it_cur + 1;
	while (it_next != path.end()){
		length += it_cur->second * (it_next->first - it_cur->first);
		it_next++;
		it_cur++;
	}
	return length / t;
}

int queue::count_empty_queue(){
	/* count how many times a customer appears on an empty queue */
	int count=0, previous;
	vector<pair<double, int>>::const_iterator it = path.begin();
	previous = it->second;
	it++;
	while(it != path.end()){
		if (it->second==1 && previous==0) 
			count++;
		previous = it->second;
		it++;
	}
	return count;
}