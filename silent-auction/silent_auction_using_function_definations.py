# def info(bider):
#     name = input('Enter the name of the bider: ')
#     amount = int(input('Enter the bid value: '))

#     bider[name] = amount
#     return bider 

# def repeat():
#     repeat_again = input('are there any other bider[y/n] : ').lower()
#     if repeat_again not in ['y','n']:
#         print("invalid input")
#         return repeat()

#     if repeat_again == 'y':
#         return  True
#     else : return False
                    
# def winner(bider):
#     name =''
#     maxi = 0
#     for i in bider :
#         value = bider[i]
#         if value > maxi:
#             name = i
#             maxi = value 
#     print(f'winner is {name} with the amount {maxi}')


# bider = {}
# while True :
#     bider = info(bider)
    
#     if not repeat():
#         winner(bider)
#         break



        

def info(bider):
    name = input('Enter the name of the bidder: ')
    amount = int(input('Enter the bid value: '))
    bider[name] = amount
    return bider 

def repeat():
    repeat_input = input('Are there any other bidders [y/n]: ').lower()
    if repeat_input not in ['y', 'n']:
        print("Invalid input. Please enter 'y' or 'n'.")
        return repeat()  
    return repeat_input == 'y'

def winner(bider):
    name = ''
    maxi = 0
    for i in bider:
        value = bider[i]
        if value > maxi:
            name = i
            maxi = value 
    print(f'Winner is {name} with the amount ₹{maxi}')

bider = {}
while True:
    bider = info(bider)
    
    if not repeat():
        winner(bider)
        break
