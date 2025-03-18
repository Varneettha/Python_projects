# #A stack is a fundamental data structure in computer science that works on the principle of Last In, First Out (LIFO). This means the last item added to the stack is the first one to be removed, similar to a stack of plates or books where you can only remove or add items from the top.

# Key Concepts
# Push: Adding an element to the top of the stack.

# Pop: Removing the topmost element from the stack.

# Peek/Top: Viewing the topmost element without removing it.

# IsEmpty: Checking whether the stack is empty.

stack = []

# Push elements
stack.append('A')
stack.append('B')
stack.append('C')
print(stack)

# Peek at the top element(last elemnt)
print(stack[-1])  # Output: 'C'

# Peek at the top element(last elemnt)
print(stack[-2])

# Pop elements
stack.pop()  # Removes 'C'
print(stack)  # Output: ['A', 'B']

# Check if stack is empty
print(len(stack) == 0)  # Output: False
