x=input("Enter format for palindrome(string/integer): ")
if x=="integer":
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
else:
    a=input("Enter the string: ")
    a=a.casefold()
    rev_a=reversed(a)
    if list(a)==list(rev_a):
        print("The given string is a palindrome")
    else:
        print("The given string is not a palindrome")
