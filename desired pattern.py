a=input("Enter the character to be displayed: ")
n=int(input("Enter the number of times to be displayed: "))
for i in range(0,n):
   for j in range(0,i+1):
      print(a ,end=" ")
   print("\r")
