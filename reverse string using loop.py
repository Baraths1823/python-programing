def reverse(str):
    str1=""
    for i in str:
        str1=i+str1
    return str1
str=input("Enter the string: ")
print("The Reversed string is: ",reverse(str))
