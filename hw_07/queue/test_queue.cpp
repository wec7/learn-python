/*
Copyright: Copyright (C) 2014 Baruch College MTH9815 Software Engineering
Description: use a monte Carlo Simulation to simulate a Queue at a supermarket.
Usage: make
Author: Weiyi Chen, Yun Peng
*/

#include "queue.h"

int main(int argc, char const *argv[])
{
	// Simulate a path of 1000 minutes at 10 seconds intervals. 
	queue queue(1000 * 60);
	
	/*
	Assume a Poisson distribution for the arrival with lambda = 0.33333 (per minute) and 
	departure (to through the cash) with lambda = 0.66666 (per minute). 
	*/
	queue.monteCarlo_simulation(1.0/3/60, 2.0/3/60); 

	// - how many times a customer appears on an empty queue (Q =1, 2, etc).
	cout << "The number of times a customer appears on an empty queue is: " << queue.count_empty_queue() << endl;

	// - what is the average queue length?
	cout << "The average queue length is: " << queue.avg_queue_len() << endl;

	return 0;
}