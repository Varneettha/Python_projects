#A lambda function in Python is an anonymous (unnamed) function declared using the lambda keyword. Unlike a standard function defined with def, lambda functions:
square = lambda x: x ** 2
print(square(4))  # Output: 16
#with multiple arguements
multiply = lambda x, y: x * y
print(multiply(3, 5))  # Output: 15


#map_function
#The map() function applies a given function to all items in an iterable (like a list or tuple) and returns a new iterable (like a map object). 
# It’s used to transform data by applying the same operation to every element.
numbers = [1, 2, 3, 4]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16]
#multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = map(lambda x, y: x + y, list1, list2)
print(list(sums))  # Output: [5, 7, 9]


#filter function
#The filter() function filters elements from an iterable based on a condition defined by a function. It only includes elements for which the condition evaluates to True.
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]

words = ["apple", "banana", "cherry", "date"]
filtered_words = filter(lambda word: 'a' in word, words)
print(list(filtered_words))  # Output: ['apple', 'banana','date']
