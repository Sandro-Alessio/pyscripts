def prime_test( m ):
	i = 2
	while m%i:
		i += 1 
	if i == m:
		print m, "is a prime number."
	else:
		print m, "is no prime number."

n = input("Enter integer value: ")
prime_test( n );
