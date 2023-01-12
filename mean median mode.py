L1=[]
n1=int(input("Enter n number of list:"))
for i in range(n1):
    a=int(input("Enter the list : "))
    L1.append(a)
n = len(L1)
L1.sort()
s=sum(L1)
mean=s/n
print("mean of list is",mean)
 
if n % 2 == 0:
    median1 = L1[n//2]
    median2 = L1[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = L1[n//2]
print("Median of list is: " + str(median))

x = []
y = []
for i in L1:
    if i not in x:
        x.append(i)
    else:
        y.append(i)
print("The mode of list is ",set(y))


