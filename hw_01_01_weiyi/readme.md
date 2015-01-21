(c) 2014 Baruch College, MTH 9815.

Created on Sep 6, 2014

Author:

	Weiyi Chen, Yun Peng

Contact: 

	weiyi.alan.chen@gmail.com, yunpeng0101@gmail.com

Summary: 

	1. readme.md for mortgage_payments.py

	2. Create a program call mortgage_payments.py that given Principal, annual 
	interest rate and Term (15 or 30 years), prints to the screen 4 columns "T, 
	Balance, Payment, Principal Paid, Interest Paid" where T is the payment number.

Library:

	1. sys: exit(), argv
	2. getopt: getopt(), GetoptError
	3. numpy: np.round()
	4. pandas: DataFrame() 

Design:

	1. read_args(ls_argv): read arguments from command line

	2. mortgage_payments(f_principal, f_interestRate, i_years): construct a 
		DataFrame with 4 columns T, Balance, Payment, Principal Paid, Interest 
		Paid

		(i) Calculate monthly interest and monthly payment first

		for each payment:

			(i) Interest Paid = Balance * Monthly Interest

			(ii) Principal Paid = Monthly Payment - Interest Paid

			(iii) Balance = Balance - Principal Paid

			(iv) Record information necessary to the dataframe df_mortgage

	3. print out results df_mortgage in 2 decimals

Usage:

	python mortgage_payments.py -p <principal> -i <interest rate> -t <term>
