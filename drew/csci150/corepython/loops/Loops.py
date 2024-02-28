##########################################
print("# While Loop")# While Loop
##########################################
count = 0
while count < 3:
    count = count + 1
    print("Hello World")
##########################################
print("# Using else statement with While Loop")# Using else statement with While Loop
##########################################
count = 0
while count < 3:
    count = count + 1
    print("Hello World")
else:
    print("In Else Block")
##########################################
#print("# Infinite While Loop")# Infinite While Loop
##########################################
# count = 0
# while count == 0:
#     print("Hello World")
##########################################
print("# For Loop")# For Loop
##########################################
n = 4
for i in range(0, n):
    print(i)
##########################################
print("# Example with List, Tuple, String,")# Example with List, Tuple, String,
print("# and Dictionary Iteration Using for Loops")# and Dictionary Iteration Using for Loops
##########################################
print("List Iteration")
l = ["Drew", "CSCI", "150"]
for i in l:
    print(i)
print("\nTuple Iteration")
t = ("Drew", "CSCI", "150")
for i in t:
    print(i)
print("\nString Iteration")
s = "Drew"
for i in s:
    print(i)
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s %d" % (i, d[i]))
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),
##########################################
print("# Iterating by the Index of Sequences")# Iterating by the Index of Sequences
##########################################
list = ["Drew", "CSCI", "150"]
for index in range(len(list)):
    print(list[index])
##########################################
print("# Using else Statement with for Loop")# Using else Statement with for Loop
##########################################
list = ["Drew", "CSCI", "150"]
for index in range(len(list)):
    print(list[index])
else:
    print("Inside Else Block")
##########################################
print("# Nested Loops")# Nested Loops
##########################################
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
##########################################
print()# Continue Statement
##########################################
for letter in 'helloworld':
    if letter == 'e' or letter == 'l':
        continue
    print('Current Letter :', letter)
##########################################
# Break Statement
##########################################
for letter in 'helloworld':
    if letter == 'e' or letter == 'l':
        break

print('Current Letter :', letter)
#########################################
# Pass Statement
##########################################
for letter in 'helloworld':
    pass
print('Last Letter :', letter)
##########################################
# How for loop in Python works internally?
##########################################
fruits = ["apple", "orange", "kiwi"]

for fruit in fruits:
    print(fruit)
##########################################
# How for loop in Python works internally?
##########################################
fruits = ["apple", "orange", "kiwi"]
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break
##########################################
