#defining a func
def greet(name):
    print(f"Hello {name}")

#calliNG
greet("Jegan Sush")

#Function Parameters and Arguments
def add(a, b):
    return a + b

result = add(1, 2)
print(result)

def increment(a, b):
    return a + b
result = print(increment(1, 2))



#Default Parameters
#You can provide default values for parameters. If no argument is passed, the default value is used:
def greet(name="friend"):
    print(f"Hello, {name}!")

greet()  # Outputs: Hello, friend!
greet("Alice")

#Function Scope
#Variables defined inside a function are local to that function and are not accessible from outside:

def my_function():
    local_variable = 10
    print(local_variable)

my_function()  # Outputs: 10
#print(local_variable) ## Raises an error because `local_variable` is not defined outside the function

#Higher-Order Functions
#Functions can also accept other functions as arguments or return them:

def apply_operation(func, x, y):
    return func(x, y)

def multiply(a, b):
    return a * b

result = apply_operation(multiply, 4, 5)
print(result)

def greet_with_emoji(message):
    words = message.split(" ")
    emoji = {
    ':-)' :'😊',
    ':-(' : '☹️'
            }
    output = ""
    for word in words:
            output += emoji.get(word, word) + " "
    print(output)

greet_with_emoji(input("What is your message? "))
#exercise
