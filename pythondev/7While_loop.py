i = 1
while i <= 10:
    print(i, end=" ")#end to print in same line
    i = i + 1
    if i>10:
        break
print("\nDone") #to print in next line

#to print pattern
i = 1
while i <= 10:
    print('*' * i)
    i = i + 1
i=9
while i>0:
    print('*' * i)
    i=i-1
    if i<=0:
        break
#continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue #(loop continues without printing)
    print(i)

#Guess game
secret_no = 9
attempts = 0

while attempts < 3:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess == secret_no:
        print("You won!")
        break
    else:
        print("Try again!")

if attempts == 3 and guess != secret_no:
    print("You lost!")

#car game
user_input = input("Do you want to start the car game? (yes/no/help): ").lower()
if user_input == "yes":
    print("Let's start the car game!")
    command = input("Type 'Start/stop/quit' to proceed: ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped.")
    elif command == "quit":
        print("Game quit.")
    else:
        print("I dont understand")
elif user_input.lower() == "help":
    print('''
    Start - To start the car
    Stop - To stop the car
    Quit - To quit the game''')
    command = input("Type 'Start/stop/quit' proceed: ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped.")
    elif command == "quit":
        print("Game quit.")
    else:
        print("I dont understand")
else:
    print("Okay, see you later!")