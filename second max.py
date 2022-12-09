li=[]
a=int(input("Enter the number of elements in list: " ))
for i in range(a):
    n=int(input("Enter the list : "))
    li.append(n)
list2 = list(set(li))
list2.sort()
print("Second largest element is:", list2[-2])
