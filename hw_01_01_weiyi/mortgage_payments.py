'''

(c) 2014 Baruch College, MTH 9815.

Created on Sep 6, 2014

@author: Weiyi Chen, Yun Peng
@contact: weiyi.alan.chen@gmail.com, yunpeng0101@gmail.com
@summary: Create a program call mortgage_payments.py that given Principal, 
	annual interest rate and Term (15 or 30 years), prints to the screen 4 
	columns "T, Balance, Payment, Principal Paid, Interest Paid" where T is 
	the payment number.
@usage: python mortgage_payments.py -p <principal> -i <interest rate> -t <term>

'''
#Python imports
import sys, getopt
#3rd party imports
import numpy as np 
import pandas as pd 


def read_args(ls_argv):
	'''
	@summary: read arguments from command line
	@param ls_argv: list of auguments from command line
	@return f_principal: -p for principal (like -p 500000)
	@return f_interestRate: -i for the annual interest rate in percentage (like
		-i 3.265)
    @return i_years: -t for term in years (like -t 15)
	'''
	try:
		ls_opts, ls_args = getopt.getopt(ls_argv,"hp:i:t:")
	except getopt.GetoptError:
		print "usage: python mortgage_payments.py -p <principal> -i <interest \
		rate> -t <term>"
		sys.exit(2)
	for str_opt, str_arg in ls_opts:
		if str_opt in ("-p"):
			f_principal = float(str_arg)  # give total loan
		elif str_opt in ("-i"):
			f_interestRate = float(str_arg)  # give annual percent interest
		elif str_opt in ("-t"):
			i_years = int(str_arg)  # give length of mortgage
	return f_principal, f_interestRate, i_years


def mortgage_payments(f_principal, f_interestRate, i_years):
	'''
	@summary: construct a DataFrame with 4 columns T, Balance, Payment, 
		Principal Paid, Interest Paid
	@param f_principal: principal
	@param f_interestRate: the annual interest rate in percentage 
	@param i_years: term in years
	@return df_mortgage: DataFrame including mortgage payments
	'''
	# calculate total number of payments
	i_paymentNum = i_years * 12  
	# calculate monthly interest rate
	f_monthlyInterest = f_interestRate / (100 * 12)  
	# calculate monthly payment
	f_monthlyPayment = f_principal * (f_monthlyInterest / (1-(1+\
		f_monthlyInterest)**(-i_paymentNum)))  
	ls_balance, ls_payment, ls_principalPaid, ls_interestPaid = [], [], [], []
	f_balance, f_payment = f_principal, f_monthlyPayment
	f_principalPaid, f_interestPaid = 0., 0.
	for i in range(i_paymentNum):
		f_interestPaid = f_balance*f_monthlyInterest
		f_principalPaid = f_payment - f_interestPaid
		ls_balance.append(f_balance)
		ls_payment.append(f_payment)
		ls_principalPaid.append(f_principalPaid)
		ls_interestPaid.append(f_interestPaid)
		f_balance -= f_principalPaid
	d_mortgage = {'Balance': ls_balance, 'Payment': ls_payment, 'Principal paid':\
		ls_principalPaid, 'Interest Paid': ls_interestPaid}
	df_mortgage = pd.DataFrame(d_mortgage, index=range(1, i_paymentNum+1))
	df_mortgage = df_mortgage[['Balance', 'Payment', 'Principal paid', \
		'Interest Paid']]
	return df_mortgage


if __name__ == "__main__":
	f_principal, f_interestRate, i_years = read_args(sys.argv[1:])
	print np.round(mortgage_payments(f_principal, f_interestRate, i_years),2)
