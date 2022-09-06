def lin_reg(x, y, x_pred):
  n = len(x)
  slope = ( n*sum(i*j for i,j in zip(x,y)) - sum(x)*sum(y) ) / ( n*sum(i*i for i in x) - (sum(x))**2 )
  const = (sum(y) - slope*sum(x)) / n
  return slope*x_pred + const

import operator as op
x = [200, 250, 200, 250, 189.65, 260.35, 225, 225, 225, 225, 225, 255]
y = [43, 78, 69, 73, 48, 78, 65, 74, 76, 79, 83, 81]
x, y = zip(*sorted(zip(x, y)))
x = list(x)
y = list(y)
y_pred = []
for i in range(0, len(x)):
  y_pred.append(lin_reg(x, y, x[i]))
error = list(map(op.sub, y, y_pred))