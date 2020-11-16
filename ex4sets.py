# sets denoted by curly braces - consists of unique values only

# in below example - list contains duplicate names
all_employees = ['andre', 'mike', 'johan', 'franky', 'michelle', 'mahen', 'mildred', 'michelle', 'mahen', 'johnson', 'johan', 'andre']

# print statements below prints duplicate values and counts duplicate values also
# print(f'Total employees with DUPLICATES = {len(all_employees)}')

# to do away with duplicates the list can be turn into a set

# unique_employees = set(all_employees)
# print(f'Object type = {type(unique_employees)}')
# print(unique_employees)
# print(f'Number of Unique employees = {len(unique_employees)}')

# sets can be used to find common values in two or more sets

operational_staff = ['mahen','mildred', 'andre', 'mike']
it_staff = ['franky', 'michelle', 'mahen', 'johan', 'mike']

# to find staff in both departments:
# operational staff that is also in it department
ops_it_staff = set(operational_staff).intersection(it_staff)
print(f'OPS IT = {ops_it_staff}')

# find general staff - not working in ops or IT
general_staff = set(all_employees).difference(operational_staff, it_staff)
print(f'GENERAL STAFF = {general_staff}')

# sets can be used to find common values in two or more lists