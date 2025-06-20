import random

computer_choice = random.randint(0,2)

user_choice = int (input ("enter 0 for rock , 1 for paper , 2 for scissors : " ) )
print(f"\n coputer_choice is : {computer_choice} \n user_choice is : {user_choice}\n")

if (user_choice == computer_choice) :
    print("it is a draw")

elif ( (user_choice ==  0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0) ):
       print("computer wins")

elif user_choice not in [0,1,2]:
      print("invalid")
else:
       print("user wins")


# =================================================================================
                            # or
 # ================================================================================  



# import random

# computer_choice = random.randint(0,2)
# user_choice = int (input ("enter 0 for rock , 1 for paper , 2 for scissors : " ) )

# print(f"\n computer_choice is : {computer_choice} \n user_choice is : {user_choice}\n")

# if user_choice not in [0,1,2]:
#       print("invalid choice")
      
# elif user_choice == 2 and computer_choice == 0 :
#     print("computer wins")
# elif  user_choice == 0 and computer_choice == 2 :
#     print("user wins")

# elif user_choice == computer_choice:
#     print("it's a draw")

# elif user_choice > computer_choice :
#        print("user wins")
# else:
#             print("computer wins")       
