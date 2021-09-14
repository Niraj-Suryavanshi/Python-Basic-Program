def FactorialRecursive(n):
    if n==1 or n==0:
        return 1
    return n*FactorialRecursive(n-1)

f=FactorialRecursive(5)
print(f)        