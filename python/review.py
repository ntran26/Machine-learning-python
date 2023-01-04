# revise python basics


# list: mutable, able to change elements in a list
seq = [1,2,3,3]
print('\nFirst index is "{}"'.format(seq[0]))
seq[0] = 'new'     # assign new value to the first index of the list
print('Updated list is {} \n'.format(seq))

# tuple: immutable, unable to change elements in a tuple
tp = (3,2,3)
print('First index in the tuple is {}'.format(tp[0]))

# set: collection of unique items, never repeat duplicate items
# similar to tuples, sets are immutable
set = {1,1,1,1,2,2,2}
print('\nUnique items {}'.format(set))
set.add('hi')      # add an element to the set
print('New set is {}'.format(set))

# dictionary: consist of key and value
dict = {'key1': 'val1', 'key2': 9}
print('\nThe value of key1 is {}'.format(dict['key1']))
# nested dictionary
dict = {'k1':{'a':1,'b':2,'c':3}, 'k2':[4,5,6]}
print('Value of b in k1 is {} '.format(dict['k1']['b']))
print('Second value of k2 is {}'.format(dict['k2'][2]))

# iterate a list
seq = ['one','two','three','four','five']
for items in seq:
    # print(items)        # print all elements in the list
    print('hello')      # 5 items in the list => print 5 times

# for loop
print('\nFor loop')
for x in range(0,5):
    print(x)

# while loop
print('\nWhile loop')
x = 0
while x < 5:
    print(x)
    x += 1

# list comprehension
print('\nList comprehension')
x = [1,2,3,4]
print(x)
out = [num**2 for num in x]
print(out)

# function
def add(a,b):
    # docstring
    """     # Add
    This function adds 2 numbers\n
    Take 2 arguements
    """
    c = a + b
    return c
a = 2
b = 3
c = add(a,b)
print('\n{} + {} is {}'.format(a,b,c))

# lambda
t = lambda num: num**2
print('\nlambda replaces function: {} \n'.format(t(6)))

# map
seq = [1,2,3,4,5]
print(map(lambda num: num**2, seq))
print(list(map(lambda num: num**2, seq)))

# filter: return items based on conditions
print("\nFilter even numbers: {}".format(list(filter(lambda num: num%2 == 0, seq))))

# string methods
s = "Hello There A-hole"
print('\nString: {}'.format(s))
print('Transform to lower case: {}'.format(s.lower()))
print('Transform to upper case: {}'.format(s.upper()))
print('Split according to white space: {}'.format(s.split()))
