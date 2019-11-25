import pandas as pd
cars = pd.read_csv('cars_csv')
x = cars.drop(cars.index[5:27])
print(x)