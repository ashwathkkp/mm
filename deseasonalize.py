def compute_seasonal_index(x, num_yrs):
  four_quarter_moving_total_avg = []
  four_quarter_centered_moving_avg = []
  percent_actual_to_moving_avg = []
  # four_quarter_moving_total_avg
  j = 0
  for i in range(len(x)-3):
    temp = (x[i] + x[i+1] + x[i+2] + x[i+3]) / 4
    four_quarter_moving_total_avg.append(temp)
  #print("\nFour quarter moving averages: ", four_quarter_moving_avg)

  # four_quarter_centered_moving_avg
  for i in range(len(four_quarter_moving_total_avg)-1):
    temp = (four_quarter_moving_total_avg[i] + four_quarter_moving_total_avg[i+1]) / 2
    four_quarter_centered_moving_avg.append(temp)
  #print("\nFour quarter centered moving averages: ", four_quarter_centered_moving_avg)

  # percent_actual_to_moving_avg
  for i in range(2, len(x)-2):
    temp = (x[i] / four_quarter_centered_moving_avg[j]) * 100
    j += 1
    percent_actual_to_moving_avg.append(temp)
  #print("\nPercentage of actual to moving averages: ", percent_actual_to_moving_avg)

  # Reordering the data 
  diff = [0, 0] + percent_actual_to_moving_avg
  n = len(diff) % 4
  diff += [0 for _ in range(n)]
  #print("\nDiff values: ", diff)
  track = []
  modified_mean = []
  width = len(diff) // num_yrs
  for i in range(4):
    temp = []
    for j in range(0, num_yrs):
      temp.append(diff[width*j+i])
    track.append(temp)
  #print("\nTrack values: ", track)

  for i in range(len(track)):
    track[i] = [i for i in track[i] if i != 0]
    a = min(track[i])
    b = max(track[i])
    track[i].remove(a)
    track[i].remove(b)
    n = len(track[i])
    modified_mean.append(sum(track[i]) / n)
  #print("\nModified means / Trimmed means: ", modified_mean)
  tot = sum(modified_mean)
  adjusting_factor = 400 / tot
  seasonal_indices = []
  for i in range(len(modified_mean)):
    seasonal_indices.append(modified_mean[i] * adjusting_factor)
  #print("\nSeasonal indices: ", seasonal_indices)
  modified_seasonal_indices = [i/100 for i in seasonal_indices]
  modified_seasonal_indices = modified_seasonal_indices * num_yrs
  deseasonalized_data = []
  for i in range(len(x)):
    deseasonalized_data.append((x[i] / modified_seasonal_indices[i]))
  #print("\nDeseasonalized data: ", deseasonalized_data)

  return {'four_quarter_moving_avg':four_quarter_moving_total_avg, 'four_quarter_centered_moving_avg':four_quarter_centered_moving_avg, 'percent_actual_to_moving_avg':percent_actual_to_moving_avg, 'diff':diff, 'track':track, 'modified_mean':modified_mean, 'seasonal_indices':seasonal_indices, 'deseasonalized_data':deseasonalized_data}
  

def identify_trend(x, num_yrs):
  n = len(x)
  coding = [0 for _ in range(n)]
  mid = (n//2) - 1
  coding[mid] = -0.5
  coding[mid+1] = 0.5
  for i in range(mid-1, -1, -1):
    coding[i] = coding[i+1] - 1
  for i in range(mid+2, n):
    coding[i] = coding[i-1] + 1
  for i in range(n):
    coding[i] *= 2
  xy = [i*j for i,j in zip(coding, x)]
  x_2 = [i**2 for i in coding]
  sum_y = sum(x)
  sum_x_2 = sum(x_2)
  sum_xy = sum(xy)
  #print("\nSummation y: ", sum_y)
  #print("\nSummation xy: ", sum_xy)
  #print("\nSummation x2: ", sum_x_2)
  b = sum_xy / sum_x_2
  a = sum_y / (num_yrs * 4)
  return {'a':a, 'b':b, 'coding':coding}

actual_sales = [102, 120, 90, 78, 110, 126, 95, 83, 111, 128, 97, 86, 115, 135, 103, 91, 122, 144, 110, 98]

res = compute_seasonal_index(actual_sales, 5)
# 4 quarter centered moving average
print(f"4 quarter centered moving average : {res['four_quarter_centered_moving_avg']}")
# percentage of actual to moving average
print(f"Percentage of actual to moving averages: {res['percent_actual_to_moving_avg']}")
# modified Seasonal Indices, Seasonal Indices
print(f"Modified seasonal indices : {res['modified_mean']}")
print(f"Seasonal Indices : {res['seasonal_indices']}")
coeff = identify_trend(res['deseasonalized_data'], 5)
