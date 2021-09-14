sub1=int(input("Enter first sub 1 marks:\n"))
sub2=int(input("Enter first sub 2 marks:\n"))
sub3=int(input("Enter first sub 4 marks:\n"))
sub4=int(input("Enter first sub 4 marks:\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less than 33% in one of the subjects")
elif(sub1+sub2+sub3)/3 < 40:
    print("You are failed due to overall percentages is less than 40")   
else:
        print("Congratulations ! you are passed")     
