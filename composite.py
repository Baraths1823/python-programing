num1=int(input("Enter starting value: "))
num2=int(input("Enter ending value: "))
for i in range(num1,num2+1):
    count=0
    for j in range(2,i//2+1):
        if i%j==0:
            count+=1
    if count>=1:
        print(i)
