import random

no_of_letter = int(input("enter the number of letters:"))
no_of_symbol = int(input ("enter the number of symbols:"))
no_of_number = int(input("how many numbers:"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A' , 
           'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

num =[]
for i in range(no_of_number):
    num+= [str(random.randint(0,9))]

password = random.choices(letters,k = no_of_letter) + random.choices(symbols,k = no_of_symbol) + num
# print(password,'\n')
# print("noraml password generated is :",''.join(password))
random.shuffle(password)
print('random generated password is :', ''.join(password))

# or 
''' use random choice with for loop 
    store in a list    
    concatenate the list
    the  random shuffle 
    use for loop and concatenate each item to string '''
