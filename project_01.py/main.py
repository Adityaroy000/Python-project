# SNAKE,WATER,GUN GAME :
'''
1 for snake
-1 for water
0 for gun
'''

import random

computer = random.choice([-1,0,1])
yourch = input("Enter your choice: " )
yourDict = {"s": 1,"w":-1,"g":0}
computDict = {1:"snake",-1:"water",0:"gun"}

you = yourDict[yourch]

print(f"you chose {computDict[you]}\nComputer chose {computDict[computer]}")

if(computer == you):
    print("It's a Draw !")
else:
   ''' 
    if(computer == -1 and you == 0):
        print("You Loose :(")
    elif(computer == -1 and you == 1):
        print("You Win :)")
    elif(computer == 1 and you == -1):
        print("You Loose :(")
    elif(computer == 1 and you == 0):
        print("You Win :)")
    elif(computer == 0 and you == -1):
        print("You Win :)")
    elif(computer == 0 and you == 1):
        print("You Loose :(")
    else:
        print("Something went wrong !")
    '''

#  Or,
    
if ((computer - you) == 2 or( computer - you) == -1):
    print("You Loose :(")
else:
    print("You Win :)")