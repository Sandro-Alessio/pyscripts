import sys

f = open(sys.argv[1],'r')
print sys.argv[1],'contains:'
print len(f.readlines()),'lines'
f.close()
f = open(sys.argv[1],'r')
text = f.read()
tokens = text.split()
counter = 0
for i in tokens:
	if len(i)>1:
		counter += 1
print counter,'words'
print len(text),'chars'
