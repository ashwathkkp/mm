import math as mt
import statistics as st
import scipy.stats as ss
import operator as op

def t_test(x, y, error):
  n = len(x)
  x_mean = [st.mean(x)] * n
  x_diff = list(map(op.sub, x, x_mean))
  #x_diff = [i-j for i,j in zip(x,x_mean)]
  slope = ( n*sum(i*j for i,j in zip(x,y)) - sum(x)*sum(y) ) / ( n*sum(i*i for i in x) - (sum(x))**2 )
  SE = mt.sqrt( (sum(i**2 for i in error)/(n-2)) / mt.sqrt(sum(i**2 for i in x_diff)) )
  t_value = slope/SE
  t_table = ss.t.ppf(q=.10,df=n-2)
  return [ t_value, t_table ]
