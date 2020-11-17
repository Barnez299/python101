# strings

stringed = 'Hello World'

# print(stringed)
# print(len(stringed))
# print(stringed[:5])
# print(stringed[-5:])

# print(stringed[::-1])

# convert string to list - use SPLIT method - by default splits on " " - space
# greeting = 'Hello how are you doing'
# greeting_list = greeting.split()
# print(greeting_list)

# convert string to list - use SPLIT method - split by specific character eg - CSV files
greeting = 'Hello-how-are-you-doing'
greeting_list2 = greeting.split('-')
# print(greeting_list2)

# covert list back to string - USING JOIN METHOD

new_string = ' '.join(greeting_list2)
print(new_string)

var1 = 1.5
var2 = 1357

var3 = var2/var1

print(float(var3.'').'2f')