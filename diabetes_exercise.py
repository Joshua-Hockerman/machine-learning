""" Using the Diabetes dataset that is in scikit-learn, answer the questions below and create a scatterplot
graph with a regression line """

import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets

diabetes = datasets.load_diabetes()

# how many sameples and How many features?
print(diabetes.data.shape)

# What does feature s6 represent?

# print(diabetes.DESCR)

# print out the coefficient

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    diabetes.data, diabetes.target, random_state=11
)

lr = LinearRegression()

mymodel = lr.fit(X=X_train, y=y_train)

print(lr.coef_)

# print out the intercept

print(lr.intercept_)

# Use predicted to test your model predictions

predicted = mymodel.predict(X_test)

expected = y_test

# create a scatterplot with regression line

plt.plot(expected, predicted, ".")
x = np.linspace(0, 330, 100)
y = x
plt.plot(x, y)
plt.show()
