from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot

model = ARIMA(close, order=(2,0,2))
model_fit = model.fit()
residuals = model_fit.resid
residuals.plot()