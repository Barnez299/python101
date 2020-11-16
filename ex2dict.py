# dictionaries - denoted by {}
#  contains key value pairs - in " "

example_dict = {'name':'barnes', 'age':25, 'city':'sydney', 'country':'australia'}

# print all key-value pairs in dictionary
for key, values in example_dict.items():
    print(f'{key} --> {values}')

# print keys only:
for key in example_dict.keys():
    print(f'{key}')

# print values only:
for values in example_dict.values():
    print(f'{values}')

# updating dictionary

example_dict['email'] = 'barnes@mymail.me'
print(example_dict)

# deleting items from dict
# del method
del example_dict['country']
print(example_dict)

# del - using pop method (pass key in)

example_dict.pop('email')
print(example_dict)

# del - popitem removes last inserted item
example_dict.popitem()
print(example_dict)

# creating copy of dictionary - 2 methods
# using copy function
example_copy = example_dict.copy()
print(f'copy function --> {example_copy}')

# use dict function
example_copy2 = dict(example_dict)
print(f'dict function --> {example_copy2}')