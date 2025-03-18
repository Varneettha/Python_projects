numbers = [5, 9, 3, 6, 1, 29]
print(numbers)
numbers.insert(2,10) #insert needs arguements
print(numbers)
numbers.remove(5) #remove does not need arguements
print(numbers)
numbers.pop()
print(numbers)
numbers.clear()
print(numbers)

n = [1,2,3,4,5]
print(n.index(3)) #prints the index of num 3
print(n.index(4))
print(5 in n)  #prints true if 5 is in the list
print(n.count(5))  #number of times 5 is in list
print(n.sort()) #sorts and returns none
n.sort() #simply sorts
print(n)
print(n.sort(reverse=True)) #sort in descending order and returns none
n.sort(reverse=True) #simply sorts in descending order or n.reverse() will work the same
print(n)
n1=n.copy()  #just as a backup of first list
print(n1)

#write a program to remove the duplicates in list
num=[2,2,4,6,3,4,6,1]
for n in num:
    if num.count(n)>1:
        num.remove(n)
print(num)  #this code snippet removes the first iteration, it sometimes immutates

#or
num=[2,2,4,6,3,4,6,1]
uniques=[]
for n in num:
    if n not in uniques:
        uniques.append(n)
print(uniques)  #this code snippet is more reliable
