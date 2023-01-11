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

# Conditional selection
bool1 = df > 0
print('\n{}'.format(bool1))
print('\n{}'.format(df[bool1]))

# Select only TRUE rows of a selected column
bool2 = df[df['W'] > 0]
print('\nCondition W > 0:\n{}'.format(bool2))

bool3 = df[df['Z'] < 0]
print('\nCondition Z < 0:\n{}'.format(bool3))

# Similar notations
bool4 = df['X']>0
result = df[bool4]
print('\n{}'.format(result))
result = result[['Y','Z']]
print('\n{}'.format(result))

result = df[df['X']>0][['Y','Z']]
print('\n{}'.format(result))

# Multiple conditions (use symbols: & |)
bool5 = df[(df['W']>0) & (df['Y']>1)]
print('\nAND operation:\n{}'.format(bool5))
bool6 = df[(df['W']>0) | (df['Y']>1)]
print('\nOR operation:\n{}'.format(bool6))

# reset and set index
reset_idx = df.reset_index(inplace=False)
print('\nReset index:\n{}'.format(reset_idx))

newidx = 'CA NY WY OR CO'.split()
print('\n{}'.format(newidx))
df['States'] = newidx
print(df)

set_idx = df.set_index('States',inplace=False)
print('\nSet index:\n{}'.format(set_idx))



