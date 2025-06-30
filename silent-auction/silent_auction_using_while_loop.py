import os

def winner(bider):
    name = ''
    maxi = 0
    for i in bider:
        value = bider[i]
        if value > maxi:
            name = i
            maxi = value 
    os.system('clear')
    print('Name of the biders with values bidded are  : \n \n',bider)
    print(f'\nWinner is {name} with the amount ₹{maxi}\n')

bider={}
while True:
    name = input('Enter the name of the bidder: ')
    amount = int(input('Enter the bid value: '))
    bider[name] = amount

    repeat = input('Are there any other biders[y/n]: ').lower()
    if repeat == 'n':
        winner(bider)
        break
    elif repeat == 'y':
        os.system('clear')
    # else:
    #     print('invalid input')

