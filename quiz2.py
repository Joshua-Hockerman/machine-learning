import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier

animals = pd.read_csv("animal_classes.csv")

animals_test = pd.read_csv("animals_test.csv")

animals_train = pd.read_csv("animals_train-1.csv")

knn = KNeighborsClassifier()

# print(animals.head(3))
# print(animals_test.head(3))
# print(animals_train.head(3))
# print(type(animals_train))

animals_train_X = animals_train.loc[:, "hair":"catsize"]
animals_train_y = animals_train.loc[:, "class_number"]

animals_test_X = animals_test.loc[:, "hair":"catsize"]
animals_test_y = animals_test.loc[:, "animal_name"]

# print(animals_train_X.head(3))
# print(animals_train_y.head(3))

knn.fit(animals_train_X, animals_train_y)

predicted = knn.predict(animals_test_X)

expected = animals_train_y

# print(predicted[:20])
# print(list(expected[:20]))

predicted_classes = [animals.Class_Type[x - 1] for x in predicted]

animal_names = list(animals_test_y)

zipped_animals = []

for a, p in list(zip(animal_names, predicted_classes)):
    new_list = [a, p]
    zipped_animals.append(new_list)

# print(zipped_animals)

animal_df = pd.DataFrame(zipped_animals)

animal_df.columns = ["animal_name", "prediction"]

# print(animal_df)

animal_df.to_csv("predictions-hockerman.csv", index=False)
