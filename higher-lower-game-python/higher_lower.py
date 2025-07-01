import logo
import data_base
import random
import os

def clear_screen():
    os.system('clear')

def display(info):
    for key, value in info.items():
        if key != 'count':
            print(f"{key}: {value}")


def game(a,b,score):
    print(logo.higher)
    print(f"\nYOUR SCORE : {score}\n")

    print("1)")
    display(a)

    print(logo.vs)

    print("2)")
    display(b)

    popular = max(a['count'],b['count'])
    
    while True:
        try:
            user_input = int(input("\nwho is popular?(1 or 2) : "))
            if user_input in [1,2]:
                break
            else : 
                continue
        except ValueError:
            print('\nPlease enter number')    

    clear_screen()

    choice = a['count'] if user_input == 1 else b['count']

    if choice == popular:
        score += 1
        print(' Correct '.center(30,"="),'\n')
    else :
        print(' Wrong '.center(30,"="),'\n')

    return b,score

a,b = random.sample(data_base.data,2)
score = 0

for i in range(5):
    a,score = game(a,b,score)

    while True:
        b= random.choice(data_base.data)
        if b != a:
            break

print('Game over'.center(30,'='))
print(f"YOUR SCORE IS : {score}".center(30))
print('='*30)
    
