try:
    # Code that might cause an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if a ZeroDivisionError is encountered
    print("Oops! Division by zero is not allowed.")
#Steps:
#try: Contains the code that might raise an exception.

#except: Contains the code that runs if the specified exception happens.

#More Examples:
#Handling Different Exceptions:
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("Oops! Division by zero is not allowed.")
except ValueError:
    print("Invalid input. Please enter a number.")

#ZeroDivisionError: Raised when attempting to divide by zero.
#ValueError: Raised when the input cannot be converted to an integer.

#Using else and finally:
#The else block runs if no exception is raised. The finally block runs no matter what, often used for cleanup actions like closing files.


try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("Oops! Division by zero is not allowed.")
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    print(f"Success! The result is {result}.")
finally:
    print("This block runs no matter what.")

#Explanation:
#else Block: Only runs if the try block does not raise an exception. In the example, it prints the result if the user input and division are successful.

#finally Block: Runs whether an exception is raised or not, used here to print a message at the end.

#Raising Exceptions:
#Sometimes, you’ll want to raise an exception yourself. Use the raise keyword.


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")


#Function divide: Raises a ValueError if attempting to divide by zero.

#try Block: Calls divide and catches the ValueError, printing the error message.

#Summary:
#try Block: Put the code that might throw an error.

#except Block: Handle specific exceptions that might arise.

#else Block: Run code if no exceptions occur.

#finally Block: Always runs, used for cleanup.

#By understanding these basics and seeing examples, you can start writing code that handles errors smoothly, making your programs more resilient and user-friendly. 😊 Want to explore more or see another example?

