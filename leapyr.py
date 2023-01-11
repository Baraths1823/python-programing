a=int(input("enter the year:"))
b=a-(a%4)
if a%4==0:
    print(a,"is leap year")
else:
    print(a,"is not leap year")
    print(b,"is leap year" ,"and", b+4, "is leap year")
