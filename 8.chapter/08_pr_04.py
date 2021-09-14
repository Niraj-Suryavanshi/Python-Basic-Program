n=int(input("Enter a  number "))

def recurSum(n):
    for i in range(n):
        if n==1 or n==0:
            return 1
        sum=n+recurSum(n-1)
        return sum

final=recurSum(n) 
print(final)