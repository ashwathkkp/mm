def lagranges(x, f, x_pred):
  res = 0
  for i in range(0, len(f)):
    coef = 1
    for j in range(0,len(f)):
      if j != i:
        coef = coef * (x_pred - x[j])/(x[i]-x[j])
    res = res + coef*f[i]
  return res

x = [0, 1, 2, 5.5, 11, 13, 16, 18]
f = [0.5, 3.134, 5.3, 9.9, 10.2, 9.35, 7.2, 6.2]

x_pred = 0.5
y_pred = lagranges(x, f, x_pred)
print(y_pred)
x_pred = 3
y_pred = lagranges(x, f, x_pred)
print(y_pred)