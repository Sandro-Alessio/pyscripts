a = 0
b = 1
c = 1

print "%10s %30s" % ("F_n","(F_n+1)*(F_n-1)-(F_n)^2")
print "%10d" % ( a )

for i in range(20):
	print "%10d %30d" % ( b, c*a-b*b )
	a = b
	b = c
	c = a + c
