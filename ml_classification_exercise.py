# The Iris dataset is referred to as a “toy dataset” because it has only 150 samples and four features.
# The dataset describes 50 samples for each of three Iris flower species—Iris setosa, Iris versicolor and Iris
# virginica. Each sample’s features are the sepal length, sepal width, petal
# length and petal width, all measured in centimeters. The sepals are the larger outer parts of each flower
# that protect the smaller inside petals before the flower buds bloom.

# EXERCISE
# load the iris dataset and use classification
# to see if the expected and predicted species
# match up

from pandas.core.frame import DataFrame
from sklearn.datasets import load_iris

iris = load_iris()

# print(iris.DESCR)

print(iris.data[5])

print(iris.target)

print(iris.target_names)

# display the shape of the data, target and target_names

print(iris.data.shape)

print(iris.target.shape)

print(iris.target_names.shape)

# display the first 10 predicted and expected results using
# the species names not the number (using target_names)

from sklearn.model_selection import train_test_split

data_train, data_test, target_train, target_test = train_test_split(
    iris.data, iris.target, random_state=11
)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

knn.fit(X=data_train, y=target_train)

predicted = knn.predict(X=data_test)

expected = target_test

predicted = knn.predict(X=data_test)

expected = target_test

predicted = [iris.target_names[x] for x in predicted]
expected = [iris.target_names[y] for y in expected]

print(predicted[:20])
print(expected[:20])

# display the values that the model got wrong

wrong = [(pred, exp) for (pred, exp) in zip(predicted, expected) if pred != exp]

print(wrong)

# visualize the data using the confusion matrix

from sklearn.metrics import confusion_matrix

confusion = confusion_matrix(y_true=expected, y_pred=predicted)

import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

confusion_df = DataFrame(confusion, index=iris.target_names, columns=iris.target_names)

figure = plt.figure(figsize=(3, 3))
axes = sns.heatmap(confusion_df, annot=True, cmap=plt.cm.nipy_spectral_r)
plt.xlabel("Expected")
plt.ylabel("Predicted")
plt.show()
