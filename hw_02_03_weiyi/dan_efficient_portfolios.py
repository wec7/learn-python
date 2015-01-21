import argparse
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import pandas as pd 
import pandas.io.data as web
import numpy as np
from numpy.linalg import inv

def read_arg():
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', action="store", \
		default=date.today().strftime("%Y%m%d"))
	parser.add_argument('-f', action="store", default="symbols.txt")
	parser.add_argument('-i', action="store", default=0.03/252, type=float)
	parser.add_argument('-r', action="store", default=0.05/252, type=float)
	parser.add_argument('-v', action="store", default=0.2/np.sqrt(252), type=float)
	return parser.parse_args()

def read_data(dt_start, dt_end, ls_symbols):
	pan_data = web.DataReader(ls_symbols, 'yahoo', dt_start, dt_end)
	df_close = pan_data['Adj Close']
	return df_close

def calculate_weights(df_close, read_arg):
	df_rets = df_close.shift(-1) / df_close - 1
	df_rets = df_rets.drop(df_rets.index[-1])
	df_norm = df_rets - df_rets.mean()
	mat_mu = np.matrix(df_rets.mean() - read_arg.i).transpose()
	mat_cov = np.matrix(df_norm.cov())
	mat_ones = np.matrix(np.ones(len(df_rets.columns)))
	mat_weightT = 1./float(mat_ones*inv(mat_cov)*mat_mu) * inv(mat_cov) * mat_mu
	if read_arg.r != None: 
		mat_weightCash = 1 - (read_arg.r - read_arg.i)/float(mat_mu.transpose()*\
			mat_weightT)
		print mat_weightCash
	elif read_arg.v != None:
		mat_weightCash = 1 - read_arg.v/np.sqrt(mat_weightT.transpose()*mat_cov*\
			mat_weightT)*np.sign(mat_ones*inv(mat_cov)*mat_mu)
	#print mat_weightCash
	mat_weight = (1-float(mat_weightCash))*mat_weightT
	df_weight = pd.DataFrame(mat_weight, index=ls_symbols, columns=['Weight'])
	return df_weight

dt_end = datetime.strptime(read_arg().d, "%Y%m%d")
dt_start = dt_end + relativedelta(months=-3)
ls_symbols = open("symbols.txt").read().split('\n')
df_close = read_data(dt_start, dt_end, ls_symbols)
print calculate_weights(df_close, read_arg())