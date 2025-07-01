
import random
import os 

def guess():
    print('Let me think of a number between 1 to 50....\n')
    level = input("Enter the diffuculty level 'H' for Hard and 'E' for Easy : ").upper()
    if level == 'H':
        attempts = 5
    else :
        attempts = 10

    num = random.randint(1,51)
    print(num)

    while attempts >=1 :
        try:
            choice = int(input('\nGuess the Number : '))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue
        if num == choice:
            print(f'\nYou Have Guessed Right..\n\n')
            print(" YOU WIN ".center(15,'*'),'\n') 
            return

        attempts -= 1
        os.system('clear')
        if num > choice:
            print(f"Your Guessed number is low... try again \n You have {attempts} attempts left")
        else:
            print(f"Your Guessed number is High... try again \n\nYou have {attempts} attempts left")
    os.system('clear')
    print("\nYou  are out of attempts......\n\n You Loose")
    print(f'\nThe number was : {num}\n')

guess()