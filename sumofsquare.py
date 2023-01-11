list=[]
i=int(input("numbers of list you want "))
for i in range(i):
    n=int(input("enter the list"))
    list.append(n)
a= sum(i**2 for i in list)
print("the sum of squares in the list is",a)
