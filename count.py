n=int(input("Enter the Number: "))
count=0
for i in str(n):
    n=n//10
    count=count+1
print("The count of numbers of digits is: ",count)
