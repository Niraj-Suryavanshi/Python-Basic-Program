def removeAndSplit(string,word):
    newStr=string.replace(word,"")
    return newStr.strip()

this ="      Harry Coder Tech       "
n=removeAndSplit(this,"Harry")
print(n)