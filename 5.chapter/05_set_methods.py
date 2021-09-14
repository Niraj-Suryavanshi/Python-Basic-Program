# empty set create using below syntax
b=set()
print(type(b))

b.add(5)
b.add(9)
print(b)
#cant add list or dictionary in the set
#adding repeatedly cant change the set
print(len(b))
b.remove(5)
print(b)
b.add((4,3,5))
print(b)
b.add(92)
b.add(922)
b.add(921)
print(b)

print(b.pop)
print(b)