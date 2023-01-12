n=int(input("Enter the n number of names: " ))
L=[]
for a in range(n):
    a=input("Enter the names: ")
    L.append(a)
order=input("Enter the Order(A/D): ")
if order=="A":
    print(*sorted(L),sep="\n")
elif order=="D":
    L.sort(reverse = True)
    print(*L,sep="\n")
