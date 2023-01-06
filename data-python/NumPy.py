import numpy as np

# transform a list to array
lst1 = [1,2,3,4,5]
arr1 = np.array(lst1)
print('\n1D array: {}\n'.format(arr1))

lst2 = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = np.array(lst2)
print('2D array:\n {}\n'.format(arr2))

# create an array in a range
arr3 = np.arange(0,10,2)        #  (start, stop, step)
print('Range 0 to 10, step=2: {}\n'.format(arr3))

# linspace
arr4 = np.linspace(0,10,20)      # (start, stop, number of points)
print('linspace:\n {}\n'.format(arr4))

# create an array of zeros or ones
arr5 = np.zeros(5)
print('1D zeros array: {}\n'.format(arr5))
arr6 = np.ones((3,5))
print('2D ones array:\n {}\n'.format(arr6))

# create identity matrix
arr7 = np.eye(4)
print('4x4 identity matrix:\n {}\n'.format(arr7))

# random methods
arr8 = np.random.rand(5)
print('1D random array 0-1: {}\n'.format(arr8))
arr9 = np.random.randn(2,3)
print('2x3 random array 0-1:\n {}\n'.format(arr9))
arr10 = np.random.randint(0,100,2)      # (lower, upper, number of values)
print('Random integer 0-100: {}\n'.format(arr10))

# reshape
arr = np.random.randint(-50,50,25)
print('Original:\n {}\nReshape:\n {}\n'.format(arr,arr.reshape(5,5)))

# copy array
arr_copy = arr.copy()
# print(arr_copy)

# max and min
print('Array: {}\n'.format(arr))
print('Minimum value: {}'.format(arr.min()))
print('Minimum index: {}\n'.format(arr.argmin()))
print('Maximum value: {}'.format(arr.max()))
print('Maximum index: {}\n'.format(arr.argmax()))

# array selection/indexing
arr = np.arange(0,16,1)
print('Array:\n {}\n'.format(arr))
print('{}\n'.format(arr[2:6]))
print('{}\n'.format(arr[13:]))

arr = arr.reshape(4,4)
print('{}\n'.format(arr))
print('{}\n'.format(arr[1:,:3]))

# conditional selection
arr = np.arange(1,11)
print('Array: {}\n'.format(arr))
bool_arr = arr > 3
print('Bool_arr: {}\n'.format(bool_arr))
print('Values > 3: {}\n'.format(arr[arr > 3]))

# Math operations
arr1 = np.arange(0,12)
arr2 = np.random.randint(1,50,12)
print('Array 1: {}'.format(arr1))
print('Array 2: {}\n'.format(arr2))
# Math operations between 2 arrays must be same size
print('Addition: {}\n'.format(arr1 + arr2))
print('Multiplication: {}\n'.format(arr1 * arr2))



