num1=int(1)
num2=int(50)
print("the composite numbers between 1 to 50 is")
for i in range(num1,num2+1):
    count=0
    for j in range(2,i//2+1):
        if i%j==0:
            count+=1
    if count>=1:
        print(i)
