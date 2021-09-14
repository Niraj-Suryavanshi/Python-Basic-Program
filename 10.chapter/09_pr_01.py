class Programmer:
    company="Microsoft"
    
    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getInfo(self):
        print(f"The name of {self.company} programmer working at {self.product} is {self.name}")

harry=Programmer("harry","Skype")
alka=Programmer("alka","github")
harry.getInfo()
alka.getInfo()


