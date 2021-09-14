class Calculator:
    def __init__(self,number):
        self.number=number

    def square(self):
        print(f"The square of {self.number} is {self.number **2 }")

          

    def squareRoot(self):
        print(f"The cuberoot of {self.number} is {self.number **0.5 }")


    def cube(self):
        print(f"The cube of {self.number} is {self.number **3 }")
   

obj=Calculator(4)
obj.square()
obj.squareRoot()
obj.cube()