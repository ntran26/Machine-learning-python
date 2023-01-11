import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

print(pd.Series(my_data,labels))
print(pd.Series(labels,my_data))

ser1 = pd.Series([1,2,3,4],['USA','Germany','Russia','Japan'])
print(ser1)
ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
print(ser2)

print('Index USA is: {}'.format(ser1['USA']))

ser3 = pd.Series(labels)
print('Index 0 is: {}'.format(ser3[0]))

print('ser1 + ser2 is:\n{}'.format(ser1+ser2))
