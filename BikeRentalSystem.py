class bikeshop:
    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print("Total Bikes",self.stock)
    def rentforbike(self,Q):
        if Q<=0:
            print("Enter the positive value or greater than Zero")
        elif Q>self.stock:
            print("Enter the value less than Stock")
        else:
            print("Total price",Q*100)
            print("Total Remaining stock",self.stock-Q)
while True:
    object=bikeshop(100)
    userchoice=int(input('''
    1 Display Stock
    2 Rent a bike
    3 Exit
    '''))
    if   userchoice==1:
            object.displaybike()
    elif userchoice==2:
            n=int(input("Enter the Quantity:-"))
            object.rentforbike(n)
    else:
            break