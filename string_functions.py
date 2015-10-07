f = open('kant.txt')
fm = open('kant_modified.txt','w')
text = f.read()
print 'kant.txt contains',len(text),'chars.'
fm.write(text.lower())
print 'kant.txt countains',text.count('Vernunft'),'times the word Vernunft.'
