from itertools import product

import numpy as np
from sklearn.linear_model import LinearRegression

rost = [[140], [150], [160], [170], [180]]
ves =  [40, 50, 60, 70, 80]

model = LinearRegression()

model.fit(rost, ves)

x = model.predict([[1001]])

print(x)