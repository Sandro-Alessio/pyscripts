n = input("Enter an integer value: ")
print "Prime numbers from 2 to", n ,":"

num = [True]*(n+1)

for i in range(2,n):
	if num[i]:
		j=2
		while j*i <= n :
			num[j*i] = False
			j += 1
		print i,
