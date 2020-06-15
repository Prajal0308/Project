import random
print("                      Welcome to the Game of 7 Up 7 Down! Double your coins everytime you win")


h=50
print("You have 50 Coins initially")


while True:
    a=input("do you want to play this game?(y/n):")

    if(a=='y'):
        b=int(input("how many coins do you want to Bet for?:"))
        if(b<=h):
            c=input("will the number be greater than 7,equal to 7 or less than 7?(g,e,l):")
            
            d=random.randint(1,6)
            print("first value:",d)
            e=random.randint(1,6)
            print("second value:",e)
            f=d+e
            print("your total value is",f)
            
            if(c=='g'):
                if(f>7):
                    print("Congrats,You Won!")
                    h=h-b
                    h=b*2+h
                    print("Total coins:",h)
                    
                else:
                    h=h-b
                    print("Better luck next time!")
                    print("Coins Left:",h)
                     
            if(c=='e'):
                if(f==7):
                    print("Congrats,You Won!")
                    h=h-b
                    h=b*4+h
                    print("Total Coins:",h)
                else:
                    h=h-b
                    print("Better luck next time!")
                    print("Coins Left:",h)

            if(c=='l'):
                if(f<7):
                    print("Congrats,You Won!")
                    h=h-b
                    h=b*2+h
                    print("total coins",h)
                else:
                    h=h-b
                    print("Better luck next time!")
                    print("Coins Left:",h)

    elif(a=='n'):
        print("okay bye dude :)")



















                 
                

    

    

