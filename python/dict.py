# revise python basics


# list: mutable, able to change elements in a list
list = [1,2,3,3]
print('\nFirst index is "{}"'.format(list[0]))
list[0] = 'new'     # assign new value to the first index of the list
print('Updated list is {} \n'.format(list))

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
print(dict['k1']['b'])
print(dict['k2'][2])