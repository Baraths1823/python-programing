L=[]
X=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    L.append(b)
for i in L:
    if (i%5==0) or (i%7==0):
        print(i)
        X.append(i)
print("the numbers are:" , X)
