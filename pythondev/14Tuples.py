# Creating a tuple
my_tuple = (1, 2, 3, 4)   # A tuple with four elements
print(my_tuple)
single_element_tuple = (5,) # Note the comma, this is a single-element tuple
print(single_element_tuple)
empty_tuple = ()  # An empty tuple
print(empty_tuple)

print(my_tuple[0])  # Outputs: 1
print(my_tuple[-1]) # Outputs: 4 (last element)

# Nested tuple
nested_tuple = ('apple', (2, 4, 6), 'banana')
print(nested_tuple[1][2])
print(nested_tuple[-1])
print(nested_tuple[0][1])
# Accessing the element inside nested tuple

# Concatenation
new_tuple = my_tuple + (5, 6)  # (1, 2, 3, 4, 5, 6)
print(new_tuple)

# Repetition
repeated_tuple = my_tuple * 2  # (1, 2, 3, 4, 1, 2, 3, 4)
print(repeated_tuple)

# Count the occurrences of an element
print(my_tuple.count(2))  # Outputs: 1

# Find the index of an element
print(my_tuple.index(3))  # Outputs: 2