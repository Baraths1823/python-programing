def s(n, start):
	if n == 0:
		return 1
	c= 0
	for i in range(start, 5):
		c+= s(n - 1, i)
	return c	
def v(n):
	return s(n, 0)
n =int(input("enter value of n"))
print(v(n))
