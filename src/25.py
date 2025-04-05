import numpy as np
from sklearn.linear_model import LinearRegression

def predict(x):
    # Make predictions using linear regression
    model = LinearRegression()
    model.fit(x.values.reshape(-1, 1), y)
    return model.predict(x).reshape(1, -1)[0]
