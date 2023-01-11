L = []
num = int(input("Enter number of elements in the list:"))
for i in range(0,num):
    n = int(input("Enter element:"))
    L.insert(i,n)
print("L =",L)
Set = set(L)
L = list(Set)
L.sort()
M = int(input("Mth largest value of m= "))
N = int(input("Nth smallest value of n = "))
print(M,"th largest:",L[-M])
print(N,"th smallest:",L[N-1])
