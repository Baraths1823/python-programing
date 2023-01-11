n=int(input("enter the number:"))
temp=n
sum=0
while(n>0):
    r=n%10
    sum=sum*10+r
    n=n//10
if(temp==sum):
    print("The Given number is a palindrome")
else:
    print("The Given number is not a palindrome")
    
