import statistics as st
def r2(y, error):
  sse = sum([pow(i, 2) for i in error])
  mean = st.mean(y)
  sst = sum([(i - mean)**2 for i in y])
  return 1 - (sse/sst)
