import numpy as np
from sklearn.linear_model import LinearRegression
import joblib #to save the model

x= np.array([[1],[2],[3],[4],[5]])
y= np.array([2,4,6,8,10]) # multiplying by 2

model = LinearRegression()
model.fit(x,y)

joblib.dump(model,'model.pkl')