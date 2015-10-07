m1 = [ [ 0.61, 0.24, 1.16 ], [ 0.14, -0.82, 0.92 ], [ -1.25, 0.96, -0.23 ] ]
m2 = [ [ 0.40, -0.68, -0.68 ], [ 0.65, -0.75, 0.23 ], [ 0.52, 0.51, 0.31 ] ]
l = len(m1)
m = len(m2)
n = len(m2[0])
m3 = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
	for j in range(0,3):
		for k in range(0,3):
			m3[i][j] += m1[i][k]*m2[k][j]

print "m3 = { ",
for i in range(0,3):
	print "{ ",
	for j in range(0,3):
		print m3[i][j],
	print " }",
print " }"
