class Railwayforms:
    formType="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")


harrysapplication =  Railwayforms()
harrysapplication.name="Harry"
harrysapplication.train="Rajdhani"
harrysapplication.printData()