import random as rd
def welcome():
    for i in range(0,20):
        print("*\t",end=" ")
    print()
    print("*",end=" ")
    for i in range(0,19):
        print("\t",end=" ")
    print("*")
    print("*",end=" ")
    for i in range(0,19):
        print("\t",end=" ")
    print("*")
    print("*",end=" ")
    for i in range(0,10):
        print("\t",end=" ")
    print("WELCOME",end=" ")
    for i in range(0,8):
        print("\t",end=" ")
    print("*")
    print("*",end=" ")
    for i in range(0,19):
        print("\t",end=" ")
    print("*")
    print("*",end=" ")
    for i in range(0,19):
        print("\t",end=" ")
    print("*")
    for i in range(0,20):
        print("*\t",end=" ")
    print()
    input("press any key:")

def mainmenu():
    print("1.Rock Paper Scissors\n2.Exit")
    ch=int(input("Enter your choice number:"))
    if ch==1:
        rockpaperscissorsmenu()
    elif ch==2:
        exit()
    else:
        print("invalid number")
        mainmenu()
def rockpaperscissorsmenu():
    print("1.Play\n2.Rules\n3.Return to main menu")
    ch=int(input("Enter your choice number:"))
    if ch==1:
        rockpaperscissors()
    elif ch==2:
        rockpaperscissorsrules()
    elif ch==3:
        exit()
    else:
        print("invalid number")
        rockpaperscissorsmenu()

def rockpaperscissorsrules():
    print("A player who decides to play rock will beat another player who has chosen scissors")
    print("rock crushes scissors or sometimes blunts scissors[1]), but will lose to one who has played paper |paper covers rock|")
    print("a play of paper will lose to a play of scissors |scissors cuts paper|.")
    print("If both players choose the same shape, the game is tied and is usually immediately replayed to break the tie")
    rockpaperscissorsmenu()

def rockpaperscissors():
    print("WELCOME TO ROCK, PAPER AND SCISSORS")
    print("You will computing against the computer. The player that score 5 point firt , it will be chosen be as winner")
    print("if your choice is Rock, Enter 0")
    print("if your choice is Paper, Enter 1")
    print("if your choice is Scissors, Enter 2")
    print("if you wish to exit , Enter -1")
    user=0
    comp=0
    cnt=0
    choice=["Rock","Paper","Scissors"]
    while(user<5 and comp<5 and cnt<25):
        cnt+=1
        u_ch=int(input("Enter your choice:"))
        if u_ch==-1:
            print("Thank you")
            break
        c_ch=rd.choice([0,1,2])
        if u_ch==0 and c_ch==1:
            comp+=1
        elif u_ch==0 and c_ch==2:
            user+=1
        elif u_ch==1 and c_ch==0:
            user+=1
        elif u_ch==1 and c_ch==2:
            comp+=1
        elif u_ch==2 and c_ch==0:
            comp+=1
        elif u_ch==2 and c_ch==1:
            user+=1
        print("You:",choice[u_ch])
        print("Computer:",choice[c_ch])
        print("Your score:",user,"\t Computer's Score:",comp)
    if user>comp:
        print("\nCongragulations! You win!")
    elif comp>user:
        print("\nOops!Sorry you lose. Better luck next time")
        
    else:
        print("\nMatch Draw")
    mainmenu()
        
welcome()
print("\n"*100)
mainmenu()


