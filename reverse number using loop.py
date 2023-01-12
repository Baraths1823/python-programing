n=int(input("Enter the number: "))
r=0
while n!=0:
    a=n%10
    r=r*10+a
    n//=10
print("The Reversed Number is: ",str(r))
