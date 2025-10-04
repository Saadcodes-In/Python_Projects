'''
0 for snake
1 for water 
2 for Gun'''

import random
computer = random.choice([0,1,2])
youstr = input("Enter your choice:")
dictstr = {
    's' : 0,
    'w' : 1,
    'g' : 2,
}

you = dictstr[youstr]


dic_p = {0 : 'snake'
         , 1 : 'water',
           2 : 'gun'}

choice = print(f"you chose {dic_p[you]}, computer chose {dic_p[computer]}")

if(computer == you):
    print("it's a draw!")

else:
    if(computer==1 and you == 2):
        print("You Win!")
    
    
    elif(computer==1 and you == 0):
        print("You Win!")
    
    elif(computer==2 and you == 1):
        print("You LOse!")
    
    elif(computer==0 and you == 1):
        print("You Lose!")
    
    elif(computer==2 and you == 0):
        print("You Lose!")
    
    elif(computer==0 and you == 2):
    
        print("You Win!")
    else:
        print("Something Went wrong?")
