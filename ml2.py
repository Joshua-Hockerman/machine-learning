import pandas as pd

nyc = pd.read_csv("ave_hi_nyc_jan_1895-2018.csv")

print(nyc.head(3))
print(nyc.Date.values)
print(nyc.Date.values.reshape(-1, 1))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    nyc.Date.values.reshape(-1, 1), nyc.Temperature.values, random_state=11
)

print(X_train)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X=X_train, y=y_train)

coef = lr.coef_
intercept = lr.intercept_

predicted = lr.predict(X_test)

expected = y_test

# print(predicted[:10])
# print(expected[:10])


predict = lambda x: coef * x + intercept

print(predict(2500))

import seaborn as sns

axes = sns.scatterplot(
    data=nyc, x="Date", y="Temperature", palette="winter", legend=False
)
axes.set_ylim(10.70)

import numpy as np

x = np.array([min(nyc.Date.values), max(nyc.Date.values)])
