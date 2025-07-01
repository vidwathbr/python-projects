import os

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a//b



def calculate(a,b):
    operators = {'+' : add ,
            '-' : subtract ,
            '*' : multiplication ,
            '//' : division}
    for i in operators:
        print(i)
    perform = input('\nEnter the operaton to perform: ')

    for i in operators:
        if i == perform :
            operation = operators[i]
            break

    result = operation(a,b)    
    print( f" \n{a} {i} {b} = {result}")

    next = input('\nTo Continue Press Y \n\nFor Start new Calculation Press N \n\nTo Exit Press X\n\n ').upper().title()
    os.system('clear')
    if next == 'Y':
        b = float (input ('\nEnter the number :'))

        calculate(result,b)

    elif next =='N':
        start()
    else :
        print('BYE')
        return
       
    


def start():
    a,b = map( float, input("Enter the two numbers : ").split())
    calculate(a,b)

start()