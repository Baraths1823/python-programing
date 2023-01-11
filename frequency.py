import collections
L1=[]
n1=int(input("Enter n number for first list:"))
for i in range(n1):
    a=int(input("Enter the numbers : "))
    L1.append(a)
freq=collections.Counter(L1)
print("The Frequency of given numbers are: ",freq)
