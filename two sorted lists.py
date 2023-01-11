L1=[]
L2=[]
n1=int(input("Enter n number for first list:"))
for i in range(n1):
    a=int(input("Enter the numbers : "))
    L1.append(a)
n2=int(input("Enter n number for second list:"))
for i in range(n2):
    b=int(input("Enter the numbers : "))
    L1.append(b)
L3=L1+L2
print(sorted(L3))
