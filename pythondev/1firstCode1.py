#first program
print("sushma varneetha jegan") #inside single quote or double quote it always takes as string
print('o----')  #you can either put print() or print ()  space doesnt matter
print(' ||||')
print('*' * 10)

#variables

price = 10 #space doesnt matter price = 10 or price=10 is right
price=20
print('price')
print(price)
print('price is')
print(f"price is {price}")


#variables activity

name = 'John smith'
print(f"Patient name is {name}")
age = 20
print(f"age is {age}")
patient_history = 'new'
print(f"Patient history is {patient_history}")
#or
is_new = True
print(f"is_new is {is_new}")


#Getting input

name=input('what is your name?')
print(type(name))
color=input('what is your fav color?')
birth_year=int(input('birth year:'))
print(f"Hi {name}")
print('Hi ' +  name)
print('i like '+color)
print(name + ' likes ' + color + ' color.')
print(f"my birth year is {birth_year}")

#why int function is required

a=input('a is : ')
b=input('b is : ')
print(a+b)

c=int(input('c is : '))
d=int(input('d is : '))
print(c+d)

e=float(input('e is : '))
f=float(input('f is : '))
print(e+f)

#Type conversiomn
birth_year = int(input('birth year: '))
print(type(birth_year))
age = 2025 - birth_year
print(type(age))
print(age)

#activity to convert weight in pounds to kilogram and print

weight_in_pounds=int(input('weight in pounds: '))
weight_in_kgs=weight_in_pounds*0.453592
print(f"weight in kilograms is {weight_in_kgs}")