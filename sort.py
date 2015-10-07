import sys

f = open("numbers.dat")

content = []
for line in f:
	content.append(float(line.strip()))

print "Values = ", len(content)
print "Min = ", min(content)
print "Max = ", max(content)
    
dist = 1000
value = float(sys.argv[1])

for i in content:
	if abs(i-value) < dist:
		num = i
		dist = abs(i-value)

print "Value %s is closest to %s with distance %s" %(value, num, dist)

content.sort()
for i in content:
	print i
