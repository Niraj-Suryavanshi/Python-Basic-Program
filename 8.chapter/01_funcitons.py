


def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p

marks1=[77,99,49,33]
percentage1=percent(marks1)

marks2=[92,89,99,93]
percentage2=percent(marks2)

print(percentage1,percentage2)