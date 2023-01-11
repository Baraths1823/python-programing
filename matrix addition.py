r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))
X=[]
Y=[]
res=[[0,0,0],[0,0,0],[0,0,0]]
print("Enter the entries rowwise for X:")
for i in range(r):          
    a=[]
    for j in range(c):      
         a.append(int(input()))
    X.append(a)
    print(X)
print("Enter the entries rowwise for Y:")
for q in range(r):          
    b=[]
    for w in range(c):      
         b.append(int(input()))
    Y.append(b)
    print(Y)
for i in range(len(X)):
    for j in range(len(X[0])):
        res[i][j]=X[i][j]+Y[i][j]
print("result")
for r in res:
    print(r)
