num1 = int(input(" Please Enter the First Value  : "))
num2 = int(input(" Please Enter the Second Value : "))
def gcd(a, b):
    if(b == 0):
        return a;
    else:
        return gcd(b, a % b)
Val = gcd(num1, num2)

for i in range(max(num1, num2), 1 + (num1 * num2)):
    if i % num1 == i % num2 == 0:
        lcm = i
        break
print(" ")
print("The Result:")
print(" ")
print("The LCM of", num1, "and", num2, "is", lcm)

print("The GCD of" ,num1 ,"and" ,num2,"is",Val)
