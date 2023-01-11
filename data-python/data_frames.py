import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

# Create a table/data frame
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

# Selecting columns
print('\nW column:\n{}'.format(df['W']))

# Create new column
df['new'] = df['W'] + df['Y']
print('\nNew column from W + Y:\n{}'.format(df))

# Delete 
# axis=0: rows, axis=1: columns
# inplace=True to make permanent removal
df.drop('new',axis=1,inplace=True)
print(df)

# Selecting rows
rowA = df.loc['A']
print('\nRow A is:\n{}'.format(rowA))

rowC = df.iloc[2]
print('\nThird index, or row C is:\n{}'.format(rowC))

# Select a specific value
rowB_colY = df.loc['B','Y']
print('\nValue at row B and col Y is: {}'.format(rowB_colY))

# Select a subset
ab_wy = df.loc[['A','B'],['W','Y']]
print('\nRow A and B, col W and Y is:\n{}'.format(ab_wy))