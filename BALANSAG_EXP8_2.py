import pandas as pd
cars = pd.read_csv('cars.csv')
a = cars.iloc[:5,1:11:2]
print(a)
b = cars.loc[cars['Model'] == 'Mazda RX4']
print(b)
c = cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']]
print(c)
d = cars.loc[[1,18,28],['Model','cyl','gear']]
print(d)