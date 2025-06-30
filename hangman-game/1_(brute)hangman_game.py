need_to_guess = "apple"
word = need_to_guess
l=['-'] * len(word)
life = 6

length = len(word)

while '-' in l and life !=0:
    guess = input('\nguess the letter:')

    if guess not in word:
        life = life -1
        print ('\n remaining life is :' ,life)

    else:
        for i in range(length):
            if word[i] == guess:
                l[i] = guess
                # word = word.replace(guess , '-',1)
                
        # print('\n',word)        
        print('\n',l)
        print("\n remaining life is : " ,life)

print('\n End of Game ! ')

if life == 0 :
    print('\n',l)
    print('\nyou lose')

else : print('\n',l); print('\nyou win')

    