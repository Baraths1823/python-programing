string=input("Enter the string: ")
def lastword(string):
    string2=""
    length=len(string)
    for i in range(length-1,0,-1):
        if(string[i]==" "):
            return string2[::-1]
        else:
            string2=string2+string[i]
print(len(lastword(string)))
