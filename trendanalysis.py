def cal_trend(x, y):
  a = sum(y)/len(y)
  x_coded = [(i-(sum(x)/len(x)))*2 for i in x]
  b = sum([i*j for i,j in zip(x_coded,y)]) / sum([pow(i,2) for i in x_coded])
  y_pred = [a+(b*i) for i in x_coded]
  pre_trend = [(i/j)*100 for i,j in zip(y, y_pred)]
  cyc_res = [((i-j)/j)*100 for i,j in zip(y, y_pred)]
  return [y_pred, pre_trend, cyc_res]

Year = [1989, 1990, 1991, 1992, 1993, 1994, 1995]
Boxes = [21, 19.4, 22.6, 28.2, 30.4, 24, 25]
#plt.xlabel('Year')
#plt.plot(Year, Boxes, color = 'blue')
Boxes_pred, pre_trend, cyc_res = cal_trend(Year, Boxes)
#plt.plot(Year, Boxes_pred, color = 'red')
print("Maximum Fluctuation in Percent of Trend: "+ str(Year[pre_trend.index(max([abs(i) for i in pre_trend]))]))
print("Maximum Fluctuation in Cyclic Residual: "+ str(Year[cyc_res.index(max([abs(i) for i in cyc_res]))]))
