# Arrays Using the array Module
# Python's array module provides a basic array implementation. It requires all elements to have the same data type.

# Importing the Module
# python
# from array import array
# Syntax
# python
# array(typecode, [elements])
# typecode: Specifies the type of elements in the array (e.g., integers, floats).

# [elements]: A list of initial values for the array.

# Example

from array import array

# Create an integer array
arr = array('i', [1, 2, 3, 4, 5])

# Access elements
print(arr[0])  # Output: 1

# Add an element
arr.append(6)

# Remove an element
arr.remove(3)

# Display the array
print(arr)  # Output: array('i', [1, 2, 4, 5, 6])



# 2. Arrays Using Lists
# Python lists are often used as arrays because they can hold elements of any data type and are very flexible.


# Create an array-like list
arr = [1, 2, 3, 4, 5]

# Access elements
print(arr[2])  # Output: 3

# Modify an element
arr[2] = 10

# Add or remove elements
arr.append(6)
arr.remove(1)

print(arr)  # Output: [2, 10, 4, 5, 6]




# 3. Arrays Using NumPy
# NumPy is a powerful library for numerical computing in Python. It provides multi-dimensional arrays and operations on those arrays.

# Installing NumPy
# To use NumPy, install it with pip:

# bash
# pip install numpy
# Creating Arrays

import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4])

# Create a 2D array
matrix = np.array([[1, 2], [3, 4]])

# Access elements
print(arr[0])  # Output: 1
print(matrix[1, 0])  # Output: 3
# Operations with NumPy
# Element-wise operations:


arr = np.array([1, 2, 3])
print(arr + 2)  # Output: [3, 4, 5]

# Shape manipulation:


matrix = np.array([[1, 2], [3, 4]])
print(matrix.shape)  # Output: (2, 2)
