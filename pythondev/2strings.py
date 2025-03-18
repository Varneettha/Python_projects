#stringss

course = 'Python for beginners'
print(len(course))
print(course)
course = "Python's course for beginners"
print(course)
course = 'Python course for "beginners"'
print(course)
course = '''
Hi Jeg
I love you 
Thankyou
'''
print(course)
course = 'Python for beginners'
print(course[0])
print(course[-11])
print(course[0:3])
print(course[0:])
print(course[:3])

name ="jenifers"
print(name[3:-3])

#formatted strings
first = 'john'
last='smith'
msg = first+' [' + last + '] is a coder'
print(msg)
msg = f"{first} {last} is a coder"   #formatted strings
print(msg)


#escape sequence
course  = "Python for \"beginners\"" #\", \', \\, \n
print(course)
#string methods
course='Python for beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.count('o'))
print(course.find('o'))
print(course.replace('beginners', 'Absolute beginners'))
print(course.title()) #capitalize first letter of each word
print(course.strip())
print(course.strip()[:5])
print('Python' in course)  #To check if a string contains a character (or a sequence of characters), we use the in operator

