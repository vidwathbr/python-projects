user_input_word= input("enter the word to guess:")
word = user_input_word
guessed=['-'] * len(word)
life = 6

wrongly_guessed_letters=[]

while '-' in guessed and life != 0:
    guess = input('\nguess  the letter: ')

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
                # word = word.replace(guess,'-',1)
                # break

        print('\ncurrent progress : ', ''.join(guessed))
        print(f'\nwrongly guessed letters are : {wrongly_guessed_letters}')
        print('\nremaining life : ', life)

    else:
        life -= 1
        wrongly_guessed_letters.append(guess)
        print('\ncurrent progress : ', ''.join(guessed))
        print(f"\nwrongly guessed letters are : {wrongly_guessed_letters}")
        print('\nremaining lfe is : ',life)

print('\n ******* END OF GAME ! ********* ')
print('\n correct word was : ', user_input_word)
if life == 0 :
    
    print('\n you loose')
else :
    print('\n you won \n')