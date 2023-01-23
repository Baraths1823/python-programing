a=input("enter ur grade:A/B")
b=int(input("ur salary"))
c=b*0.02+b
if b<10000 and a=="A":
    print(c+(b*0.1))
elif b<10000 and a=="B":
    print(c)
elif a=="A":
    print((b*0.1)+b)
else:
    print((b*0.05)+b)
