# def GreatestOfThree(num1,num2,num3):
#     if(num1>num2 and num1>num3):
#         print("Num1 is greater: "+str(num1))
#     elif(num2>num1 and num2>num3):
#         print("Num2 is grerater: "+str(num2))  
#     else:
#         print("Num3 is greater: "+str(num3))
# GreatestOfThree(59,999,32)
def GreatestOfThree(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m=GreatestOfThree(44,311,55)
print(m)
