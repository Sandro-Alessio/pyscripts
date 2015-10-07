def scalar_product( v1, v2 ):
	sp = 0
	for i in range(0,len(v1)):
		sp += v1[i]*v2[i]

	return sp

def vector_product( v1, v2 ):
	vp = [ v1[1]*v2[2]-v1[2]*v2[1], v1[2]*v2[0]-v1[0]*v2[2], v1[0]*v2[1]-v1[1]*v2[0] ]
	return vp

v1 = [0.3,1.8,-2.2]
v2 = [-2.5,3.8,0.4]
print "v1 = {0.3,1.8,-2.2}, v2 = {-2.5,3.8,0.4}"
print "The scalar product of v1 and v2 is: ", scalar_product(v1,v2)
vp = vector_product(v1,v2)
print "The vector product of v1 and v2 is: {",vp[0],",",vp[1],",",vp[2],"}"
