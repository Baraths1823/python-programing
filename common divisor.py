a=int(input("Enter Number 1: "))
b=int(input("Enter Number 2: "))
c=0
for i in range(1,min(a,b)+1):
    if a%i==b%i==0:
        c+=1
print(c)
