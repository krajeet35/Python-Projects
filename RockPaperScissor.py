import random
l=["Rock","Scissor","Paper"]
'''
Rock vs Paper-> Paper Wins
Rock vs Scissor-> Rock Wins
Paper vs Scissor-> Paper Wins
'''
while True:
    ucount=0
    ccount=0
    a=int(input('''
    Game Start....
    1 Start
    2 Exit
    '''))
    if a==1:
        for b in range(1,6):
            c=int(input('''
            1 Rock
            2 Scissor
            3 Paper
            '''))
            if c==1:
                d="Rock"
            elif c==2:
                d="Scissor"
            elif c==3:
                d="Paper"
            e=random.choice(l)
            if e==d:
                print("Computer Value",e)
                print("User value",d)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (d=="Rock" and e=="Scissor") or (d=="Paper" and e=="Rock") or (d=="Scissor" and e=="Paper"):
                print("Computer Value", e)
                print("User value", d)
                print("You Won")
                ucount = ucount + 1
            else:
                print("Computer Value", e)
                print("User value", d)
                print("Computer Won")
                ccount = ccount+1
        if ucount==ccount:
            print("Final Result:- Game Draw")
            print("Your Score=",ucount)
            print("Computer score=",ccount)
        elif ucount>ccount:
            print("Final Result:- You Won the Game")
            print("Your Score=",ucount)
            print("Computer score=",ccount)
        else:
            print("Final Result:- Computer Won the Game")
            print("Your Score=", ucount)
            print("Computer score=", ccount)

    else:
        break