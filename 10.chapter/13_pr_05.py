class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print("********")
        print(f"The name of the train is {self.name}")
        print(f"The fare of the train is {self.fare}")
        print("********")

    def fareInfo(self):
        print(f"The price of the ticke is Rs.{self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked!Your seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("sorry this train is currently full !")       

intercity=Train("Intercity train:22123",90,2)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()


            
        