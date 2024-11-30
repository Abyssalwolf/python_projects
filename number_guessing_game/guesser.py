import random

def guess(x):
    rn=random.randint(1,x)
    guess = 0
    while guess!=rn:
        guess=int(input(f"Enter your guess (numbers ranging from 1 and {x}): "))
        if guess<rn:
            print("Try again. Too low")
        elif guess>rn :
            print("Try again. Too high")
    print(f"Congratulations! You have guessed the number {rn} correctly")

def computer(x):
    low=1
    high=x
    feedback=""
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        print(f"Computer's guess is {guess}")
        feedback=input("Enter 'h' if the guess is too high, 'l' if the guess is too low and 'c' if the guess is correct: ").lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
        elif feedback=='c':
            print(f"Yay! Computer has guessed the number {guess} correctly")
        else:
            print("Invalid input. Please enter 'h', 'l' or 'c'")

print("Welcome to the number guessing game. Choose what you want to play:\n1. You guess the number\n2. Computer guesses the number\n3. Exit")
while True:
    ch=int(input("Enter your choice: "))
    if ch==1:
        x=int(input("Enter the maximum number you want to guess: "))
        guess(x)
    elif ch==2:
        x=int(input("Enter the maximum number you want the computer to guess: "))
        computer(x)
    elif ch==3:
        break
    else:
        print("Invalid input. Please enter 1 or 2")

        
    
