def newton_divided(x, f, order):
  res = []
  for i in range(0, len(f)-1):
    res.append((f[i+1]-f[i])/(x[i+1+(order-2)]-x[i]))
    i = i+order
  return res

def newton_divided_table(x, f):
  table = []
  table.append(f)
  for i in range(0, len(f)-1):
    table.append(newton_divided(x, table[i], i+2))
  return table

def newton_divided_eq(x_pred, x, table):
  y_pred = table[0][0]
  for i in range(1, len(table)-1):
    temp = 1
    for j in range(0, i):
      temp = temp * ( x_pred - x[j] )
    y_pred =  y_pred + (temp * table[i][0])
  return y_pred
    
x = [0, 1, 2, 5.5, 11, 13, 16, 18]
f = [0.5, 3.134, 5.3, 9.9, 10.2, 9.35, 7.2, 6.2]
table = newton_divided_table(x, f)
x_pred = 0.5
print(newton_divided_eq(x_pred, x, table))
x_pred = 3
print(newton_divided_eq(x_pred, x, table))
