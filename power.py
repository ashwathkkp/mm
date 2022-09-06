import numpy as np

def exp_reg(x, y, x_pred):
  n = len(x)
  x = list(map(np.log, x))
  y = list(map(np.log, y))
  slope = ( n*sum(i*j for i,j in zip(x,y)) - sum(x)*sum(y) ) / ( n*sum(i*i for i in x) - (sum(x))**2 )
  const = (sum(y) - slope*sum(x)) / n
  const = np.exp(const)
  return const*pow(x_pred, slope)

v = [2.27, 2.76, 3.27, 3.31, 3.7, 3.85, 4.3, 4.39, 4.42, 4.81, 4.9, 5.05, 5.21, 5.62, 5.88]
p = [2500, 365, 23700, 5491, 14000, 78200, 70700, 138000, 304500, 341948, 49375, 260200, 867023, 1340000, 1092759]

p_pred = [exp_reg(v, p, i) for i in p]

