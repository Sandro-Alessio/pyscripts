print "%15s %15s" % ("sum i^3","(sum i)^2")

sum = 0
cubicsum = 0
for i in range(200):
	sum += (i+1)
	cubicsum += (i+1)**3
	print "%15d %15d" % (cubicsum, sum**2)
