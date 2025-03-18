# In Python, a set is an unordered, mutable collection of unique elements. Sets are incredibly useful when you need to eliminate duplicate values or perform mathematical set operations like union, intersection, or difference.

# Key Characteristics of Sets
# Unordered: Sets don’t maintain the order of elements.

# Unique Elements: Duplicate values are automatically removed.

# Mutable: You can add or remove elements (although the elements themselves must be immutable, like strings, numbers, or tuples).

# Creating a Set
# You can define a set using curly braces {} or the built-in set() function:


# Using curly braces
my_set = {1, 2, 3, 4}

# Using the set() function
another_set = set([1, 2, 3, 3, 4])  # Duplicates are removed
print(another_set)  # Output: {1, 2, 3, 4}

# Empty set
empty_set = set()  # Note: {} creates an empty dictionary, not a set

# Basic Operations
# Adding Elements

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}


# Removing Elements

my_set.remove(2)  # Throws an error if 2 is not in the set
my_set.discard(3)  # Removes 3 but does not throw an error if it’s missing
print(my_set)  # Output: {1, 4}


# Check Membership

print(4 in my_set)  # Output: True
print(5 in my_set)  # Output: False



# Clearing a Set
my_set.clear()
print(my_set)  # Output: set()


# Set Operations
# 1. Union (Combining Sets)
# Returns a new set with all unique elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}



# 2. Intersection (Common Elements)
# Returns a new set with elements that are in both sets.

print(set1 & set2)  # Output: {3}


# 3. Difference (Set Subtraction)
# Returns a new set with elements in the first set but not the second.


print(set1 - set2)  # Output: {1, 2}
print(set2 - set1)  # Output: {4, 5}


# 4. Symmetric Difference (Elements in Either Set but Not Both)
# Returns a new set with elements unique to each set (no overlap).


print(set1 ^ set2)  # Output: {1, 2, 4, 5}