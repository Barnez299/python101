# lists = [] # denoted by square brackets
# stores data collection types 
# is muteable (can be changed)
# can store multiple datatypes eg ints, booleans, strings

# Example of list:

fruit_basket = ['apples', 'lemons', 'bananas', 'cherries', 'grapes', 'oranges']

print(fruit_basket)

# Total number of items in basket
print(f'total items in list = {len(fruit_basket)}')

# first item in list
print(f'{fruit_basket[0]} is the first item in list using INDEX')
print(f'{min(fruit_basket)} is the first item in list using MIN')

# last item in list
print(f'{fruit_basket[-1]} is the last item in list using NEGATIVE INDEX')
print(f'{max(fruit_basket)} is the last item in list using MAX')

# print first three items in list
print(fruit_basket[:3])

#  print last three items in list
print(fruit_basket[3:])

# find index position
print(f'Third item in list = {fruit_basket[3].upper()}')

# make copy of list
new_list = fruit_basket[:]
new_list_cpy = fruit_basket.copy()
print(f'This is using the INDEX - copy method - {new_list}')
print(f'This is using the COPY function method - {new_list_cpy}')

# create empty list
new_list2 = []
new_list2.extend(fruit_basket)
print(new_list2)

# add items to END of list
# fruit_basket.append('naartjies')
# print(fruit_basket)

# add items to SPECIFIC INDEX of list
fruit_basket.insert(3,'naartjies')
print(fruit_basket)

# remove last item from list - using POP
popped = fruit_basket.pop()
print(f'last item removed from list = {popped}')
print(fruit_basket)

# remove any item from list
remove_grapes = fruit_basket.remove('grapes')
print(fruit_basket)

# 
all_items = [1,22,33,4,5,6,7,8,9,10]

new_sort = sorted(all_items)

print(new_sort)

# print reversed list
reversed_list = all_items[::-1]

print(f'this is a REVERSED and SORTED list - {sorted(reversed_list)}')

# print part of list

items = all_items[1:5]
print(items)

# print items using step:

even_numbers = all_items[1::2]
print(f'This is a list of event sorted numbers = {sorted(even_numbers)}')

# list comprehension
even_nos = [num for num in all_items if num % 2 == 0]
print("Even numbers : ", even_nos)
