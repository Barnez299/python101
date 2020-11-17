# using time module to check time of two methods
import time

# method 1

start = time.time()
my_list = ['a'] * 1000000
my_string = ''
for i in my_list:
    my_string += i
end = time.time()
elapsed_time = end - start
print(elapsed_time)

# method 2

start = time.time()
my_list = ['a'] * 1000000
my_string = ''.join(my_list)
end = time.time()
elapsed_time = end - start
print(elapsed_time)

