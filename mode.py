list1 =[]
n1=int(input("Enter n number of list:"))
for i in range(n1):
    c=(input("Enter the list : "))
    list1.append(c)
a = []
b = []
for i in list1:
    if i not in a:
        a.append(i)
    else:
        b.append(i)
print(b)
