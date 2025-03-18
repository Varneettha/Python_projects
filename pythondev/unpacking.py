# Unpacking a tuple
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Outputs: 1
print(b)  # Outputs: 2
print(c)  # Outputs: 3

# Unpacking a list
my_list = [4, 5, 6]
x, y, z = my_list
print(x)  # Outputs: 4
print(y)  # Outputs: 5
print(z)  # Outputs: 6


#Using the Asterisk (*) for Excess Elements:
numbers = [1, 2, 3, 4, 5]
first, second, *rest = numbers
print(first)  # Outputs: 1
print(second) # Outputs: 2
print(rest)   # Outputs: [3, 4, 5]

# The asterisk can be used anywhere
first, *middle, last = numbers
print(first)  # Outputs: 1
print(middle) # Outputs: [2, 3, 4]
print(last)   # Outputs: 5

#Nested Unpacking:
nested_tuple = (1, (2, 3), 4)
a, (b, c), d = nested_tuple
print(a)  # Outputs: 1
print(b)  # Outputs: 2
print(c)  # Outputs: 3
print(d)  # Outputs: 4

#unpacking in function calls:
def my_function(w, x, y, z):
    print(w, x, y, z)

args = (1, 2, 3, 4)
my_function(*args) #here if we dont use asterisks , it takes entire args as one parameter and 3 will be missing so we use * to extract

kwargs = {'w': 1, 'x': 2, 'y': 3, 'z': 4}
my_function(*kwargs)


kwargs = {'w': 1, 'x': 2, 'y': 3, 'z': 4}
my_function(**kwargs)

#multiple return values from function
def co_ordinates():
    return 78, 179

weight, height = co_ordinates()
print(weight, height)
print(weight)
print(height)

#unpacking dictionary
dictionary = {'a': 1, 'b': 2, 'c': 3}
a, b, c = dictionary.values()
print(a)  # Outputs: 1
print(b)  # Outputs: 2
print(c)  # Outputs: 3

# Unpacking keys
a, b, c = dictionary
print(a)  # Outputs: 'a'
print(b)  # Outputs: 'b'
print(c)  # Outputs: 'c'