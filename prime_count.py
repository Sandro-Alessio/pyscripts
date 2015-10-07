def prime_test( m ):
	i = 2
	while m%i:
		i += 1 
	if i == m:
		return 1
	else:
		return 0

c = 0
n = input("Enter integer value: ")
for i in range(2,n):
	c += prime_test( i )

print "There are", c ,"prime numbers from 2 to", n , "."

