principle=float(input("Enter the principle amount:"))
time=int(input("Enter the time in years:"))
abt=input("are you senior citizen yes/no:")
if abt=="yes":
    intrest1=(principle*time*12)/100
    print("The intrest is:",intrest1)
else:
    intrest2=(principle*time*10)/100
    print("The intrest is:",intrest2)
