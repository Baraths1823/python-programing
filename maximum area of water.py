def maxArea(A, Len) :
    area = 0
    for i in range(Len) :
        for j in range(i + 1, Len) :
            area = max(area, min(A[j], A[i]) * (j - i))
    print( area)
li=[]
b=int(input("Enter the number of elements in list: " ))
for i in range(b):
    n=(input("Enter the list : ")
       li.append(n)
len1 = len(li)
print(maxArea(b, len1))
 

