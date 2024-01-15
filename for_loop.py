# fruits = ["mango", "kiwi", "apple"]
# for x in fruits:
#     print(x)


# for x in "broadway":
#     print("\n", x)

# info = {
#     'Name' : 'ABC', 
#     'Class' : 8, 
#     'Roll No.' : 7,
#     'Section' : 'A'
# }

# print(type(info))
# for x in info:
#     print(info[x])

# fruits = ['orange', 'apple','banana','lichee','kiwi']
# fruits.append('mango')
# for items in fruits:
#     if items == 'banana':
#         break
#     print(items)

# fruits = ['orange', 'apple','banana','litchi','kiwi']
# for x in fruits:
#     if x == 'litchi':
#      continue
#     print(x)

# example_list = ['it','is','an','example',1,2,3,4,5,6,7,2.4,'bro']
# for items in example_list:
#     if isinstance(items,float):
#         break
#     print(items)


# example_list = ['it','is','an','example',1,2,3,4,5,6,7,2.4,'bro']
# for items in example_list:
#     if isinstance(items,float):
#         continue
#     print(items)


# for i in range(1,11,1):
#     print(i)

# Multiplication table for a required number
# x = int(input("Enter the number of multiplication table you want"))
# for i in range(1,11):
#     print(f'{x} x {i} = {x*i}')

n = int(input("Enter the number of integers to add in the list: "))
numbers = []
for i in range(n):
    x = int(input(f'Enter the integer numbers to be added in the list: '))
    numbers.append(x)
print(f'The entered list of numbers are {numbers}')
