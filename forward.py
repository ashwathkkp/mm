import math

def forward_dif(arr):
  dif = [0] * (len(arr)-1)
  for i in range(0, len(arr)-1):
    dif[i] = arr[i+1] - arr[i]
  return dif

def forward_diff_table(an):
  delta = []
  delta.append(an)
  for i in range(0, len(an)-1):
    val = forward_dif(delta[i])
    if len(val) != 0:
      delta.append(val)
    else:
      break
  return delta

def forward_diff_eq(n, an, x):
  table = forward_diff_table(an)
  u = (x - n[0])/(n[1]-n[0])
  fx = 0
  v = 1
  for i in range(0, len(table)):
    fx += (v*table[i][0])/ math.factorial(i)
    v *= u-i
  return fx

import numpy as np

n = np.arange(1,17)
an = [3,6,11,21,32,47,65,87,112,110,171,204,241,282,325,376]
an_pred = []
error = []
table = forward_diff_table(an)
for i in range(0, len(n)):
  an_pred.append(forward_diff_eq(n, an, n[i]))
  error.append( an[i] - an_pred[i])
  

from scipy import stats

t_value,p_value=stats.ttest_ind(an, an_pred)
print(t_value, p_value)
