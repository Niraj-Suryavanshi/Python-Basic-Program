f=open('sample.txt','r')#use open fun to read the content of a file
# data=f.read()#default mode is r
data=f.read(5)#reads first five characters
print(data)
f.close()