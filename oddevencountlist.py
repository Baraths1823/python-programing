L=[]
even=[]
odd=[]
a=int(input("Enter the number of elements in list: " ))
for i in range(a):
    n=int(input("Enter the list : "))
    L.append(n)
ec=0
oc=0
for x in L:
    if x%2==0:
        ec=ec+1
        even.append(x)
    else:
        oc=oc+1
        odd.append(x)
print("The Even Elements in the list is : ",even)
print("Even count-",ec)
print("The Odd Elements in the list is : ",odd)
print("Odd count-",oc)
