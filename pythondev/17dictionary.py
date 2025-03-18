#Certainly! A dictionary in Python is a data structure that stores key-value pairs. This allows you to efficiently retrieve, add, and update data based on a unique key. Here’s a deeper dive:
#Creating a Dictionary:
#You can create a dictionary using curly braces {} with pairs separated by a colon ::

# Empty dictionary
my_dict = {}

# Pre-populated dictionary
my_dict = {'name': 'Alex', 'age': 25, 'location': 'Canada'}

print(my_dict)  # Outputs: {'name': 'Alex', 'age': 25, 'location': 'Canada'}
#Accessing Values:
#You can access dictionary values using their keys:

print(my_dict['name'])  # Outputs: Alex
print(my_dict['age'])   # Outputs: 25

#To avoid KeyError for keys that might not exist, use the .get() method:

print(my_dict.get('name'))     # Outputs: Alex
print(my_dict.get('job', 'N/A')) # Outputs: N/A if 'job' key doesn't exist


#Modifying Dictionary:
#You can add, update, or delete items:
# Adding a new key-value pair
my_dict['job'] = 'Developer'
print(my_dict)

# Updating an existing key-value pair
my_dict['age'] = 26
print(my_dict)

# Deleting a key-value pair
del my_dict['location']
print(my_dict)  # Outputs: {'name': 'Alex', 'age': 26, 'job': 'Developer'}


#Looping Through a Dictionary:
#You can loop through keys, values, or key-value pairs:
# Looping through keys
for key in my_dict.keys():
    print(key)  # Outputs: name, age, job

# Looping through values
for value in my_dict.values():
    print(value)  # Outputs: Alex, 26, Developer

# Looping through key-value pairs
for key, value in my_dict.items():
    print(key, value)  # Outputs: name Alex, age 26, job Developer


#Dictionary Methods:
#Method	Description
#.keys()	Returns a view object of all keys in the dictionary
#.values()	Returns a view object of all values in the dictionary
#.items()	Returns a view object of all key-value pairs
#.update()	Updates the dictionary with another dictionary or key-value pairs
#.pop(key)	Removes and returns the value for the specified key
#.clear()	Removes all items from the dictionary

#keys() Method:
#Returns a view object of all keys in the dictionary.
keys = my_dict.keys()
print(keys)  # Outputs: dict_keys(['name', 'age', 'city'])

#.values() Method:
#Returns a view object of all values in the dictionary.
values = my_dict.values()
print(values)  # Outputs: dict_values(['Alice', 25, 'Toronto'])

#.items() Method:
#Returns a view object of all key-value pairs.
items = my_dict.items()
print(items)  # Outputs: dict_items([('name', 'Alice'), ('age', 25), ('city', 'Toronto')])

#.update() Method:
#Updates the dictionary with another dictionary or key-value pairs.
my_dict.update({'email': 'alice@example.com', 'age': 26})
print(my_dict)
# Outputs: {'name': 'Alice', 'age': 26, 'city': 'Toronto', 'email': 'alice@example.com'}

#.pop(key) Method:
#Removes and returns the value for the specified key.
age = my_dict.pop('age')
print(age)       # Outputs: 26
print(my_dict)   # Outputs: {'name': 'Alice', 'city': 'Toronto', 'email': 'alice@example.com'}

#.clear() Method:
#Removes all items from the dictionary.

my_dict.clear()
print(my_dict)  # Outputs: {}

#write a program
Phone = input("Phone number: ")
digits = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}
output=""
for char in Phone:
    output+= digits.get(char, "!")+" "

print(output)

fruits = input("Fruits (separated by space): ").split(", ")
alphabets = {'A', 'B', 'C'}
for char in fruits:
    if char[0].upper() == 'A':
        print(f"A:{char}")
    elif char[0].upper() == 'B':
        print(f"B:{char}")
    elif char[0].upper() == 'C':
        print(f"C:{char}")


fruits = input("Fruits (separated by spaces): ").split(", ")  # Split method corrects

alphabets = {'A', 'B', 'C'}
output = {'A': [], 'B': [], 'C': []}  # Dictionary to store lists of fruits

for char in fruits:
    if char[0].upper() == 'A':
        output['A'].append(char)
    elif char[0].upper() == 'B':
        output['B'].append(char)
    elif char[0].upper() == 'C':
        output['C'].append(char)

# Print the results
if output['A']:
    print(f"A: {', '.join(output['A'])}")
if output['B']:
    print(f"B: {', '.join(output['B'])}")
if output['C']:
    print(f"C: {', '.join(output['C'])}")


#emoji converter using dictionary
message =  input("Type a message :")
words = message.split(" ")

emoji = {
    ':-)' :'😊',
    ':-(' : '☹️'
}
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)


#dictionary comprehensions

#A dictionary comprehension is a concise way to create dictionaries in Python, 
# similar to list comprehensions but for key-value pairs. It allows you to construct dictionaries dynamically using a single line of code.

squares = {x: x ** 2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


#with conditional logic
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

#transforming data
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {value: key for key, value in original.items()}
print(swapped)  # Output: {1: 'a', 2: 'b', 3: 'c'}

#using multiple iterables
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
combined = {k: v for k, v in zip(keys, values)}
print(combined)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}



