def factorial( n ):
	fac = 1
	for i in range(2,n+1):
		fac *= i
	return fac

n = input("Enter integer value: ")
print n,"! =", float(factorial( n ))
