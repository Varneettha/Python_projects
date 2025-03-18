import math


names = ['Jega', 'sush', 'viji', 'radha']
print(names)
print(names[0:2])
print(names[2:4])
print(names[0:])
print(names[:4])
print(names[::1])

names[0]='Jeg'
print(names)

#write a program to find the largest num in list
lists = [5,4,1,3,10,100]
max = lists[0]
for number in lists:
    if number > max:
        max = number
print(max)


#2D Lists , These are lists in which each items in the list is another list
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[0][2])
matrix[2][2]= 100
print(matrix)

#ti iterate over all the items in the matrix

for row in matrix:
    for num in row:
        print(num)

#enumerate 
#The enumerate() function in Python is a built-in function that allows you to loop through an iterable (like a list, tuple, or string) 
# and keep track of the index of each element at the same time. It adds a counter to the elements and returns them as pairs: (index, element).
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# If you want the index to start from a number other than 0, you can specify the start parameter:

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


#program
letters = ["a","b","c"]
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

result = [0]*100
print(result)
combined = result + letters
print(combined)
newnum = list(range(20))
print(newnum)
chars = list("Hello World")
print(len(chars))

# list unpacking
numb = [1,2,3]
first, second, third = numb
first = numb[0]
second = numb[1]
third = numb[2]

print(first)
print(second)
print(third)

#unpacking use case
numbe = [1,2,3,4,5,5,5,5,5]
#incase if you need just first two elemts to be unpacked
first1, second2, *others = numbe
print(first1)
print(others)


#unpacking usecase 2
numberi = [1,2,3,4,5,5,5,5,9]
#incase if you need just first and last elemts to be unpacked
first1, *others, last = numberi
print(first,last)
print(others)