L1=[]
n1=int(input("Enter n number for first list:"))
for i in range(n1):
    a=int(input("Enter the numbers : "))
    L1.append(a)
    
for i in range(0,n1+1):
    count=0
    for j in range(2,i//2+1):
        if i%j==0:
            count+=1
    if count>=1:
        print(i)

