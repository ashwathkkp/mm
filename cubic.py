from scipy.interpolate import CubicSpline, interp1d

T = [0, 8, 16, 24, 32, 40]
O = [14.621, 11.843, 9.870, 8.418, 7.305, 6.413]
T_pred = [4, 36]
cs = CubicSpline(T, O)
print(cs(T_pred))

