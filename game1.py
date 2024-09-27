import random

computer = random.choice([-1,0,1])
print ('''s - snake
w - water
g - gun ''')

yourchoice = input ("now choose between s,w,g : ")
yourdict = {"s":1 , "w":-1 , "g":0}
reversedict = {1:"snake" , -1:"water" , 0:"gun"}

you = yourdict[yourchoice]

print(f"you chose {reversedict[you]} \ncomputer chose {reversedict[computer]}")

if computer==you:
    print("Its a tie")

else:
    if computer==-1 and you==1 :
        print("you win!")
    elif computer==-1 and you==0 :
        print("you lose!")
    elif computer==1 and you==-1 :
        print("you lose!")
    elif computer==1 and you==0 :
        print("you win!")
    elif computer==0 and you==-1 :
        print("you win!")
    elif computer==0 and you==1 :
        print("you lose!")
    else:
        print("something is wrong!")