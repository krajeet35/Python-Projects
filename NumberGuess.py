import random
a=random.randrange(1,101)
b=eval(input("Enter your Number:-"))
if a>b:
    print("Random Number", a)
    print("Your guessing number is lower")
elif a<b:
    print("Random Number", a)
    print("Your guessing number is higher")
else:
    print("Random Number", a)
    print("Congratulations !!  Your guessing number matched")