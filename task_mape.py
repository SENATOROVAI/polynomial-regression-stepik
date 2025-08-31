import numpy as np

y_true = np.array([100, 200, 300, 400])
y_pred = np.array([110, 190, 310, 390])

mape = np.mean(np.abs((y_true - y_pred)))
