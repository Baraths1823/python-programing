a=5
sum1=[]
for i in range(1,5):    
    for j in range(i):       
        print(a,end=" ")
        sum1.append(a)
    print()
    a*=2
sum1.pop(len(sum1)//2)
s=0
for i in sum1:
    s+=i
print(s)
