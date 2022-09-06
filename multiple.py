import numpy as np

def multiple_lin_reg(x,y, x_pred):
  b = np.matmul(np.linalg.inv(np.matmul(x.transpose(), x)), np.matmul(x.transpose(), y))
  return np.multiply(np.repeat([b], repeats = x_pred.shape[0], axis = 0), x_pred).sum(axis=1)

x1 = np.array([1.26926382, -9.43542734, 7.59084266, 7.52067092, -13.94486326,  11.63625102,   9.56782929 ,  1.87002637 ])
x2 = np.array([-8.97613991, 1.26926382, -9.43542734, 7.59084266, 7.52067092, -13.94486326,  11.63625102,   9.56782929])
y = np.array([ -9.43542734, 7.59084266, 7.52067092, -13.94486326,  11.63625102,   9.56782929 ,  1.87002637,  -7.09845358])

x0 = np.ones(len(x1))
x = np.stack((x0,x1,x2), axis = 1)
y_pred = multiple_lin_reg(x, y, x)
print(y_pred)