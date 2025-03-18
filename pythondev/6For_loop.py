for item in 'Python':
    print(item)

for item in [1,2,3]:
    print(item)

for item in ['Jeg', 'sush', 'baby']:
    print(item)

for item in range(10):
    print(item)

for item in range(5,10):
    print(item)

for item in range(10,0,-2):
    print(item)

for item in range(0,10,5):
    print(item)

#activity
prices = ['1000', '2000', '3000']
total = 0
for price in prices:
    total+=int(price)  #total = total+price
    if price == max(prices):
        print(f"total is {total}")


#nested loops
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

#print f shape

number = [1,1,1,1,6]
for num in number:
    output =''   #empty string
    for i in range(num):
        output+='X'
    print(output)


number = [5,2,5,2,2]
for num in number:
    output =''
    for i in range(num):
        output+='X'
    print(output)






