names =  open('p022_names.txt')
mylist = []
for line in names:
	mylist=(line.split(','))
map(lambda x: x[2:-2] ,mylist)
print mylist
dict = {'A':1,'B':2,'C':3}
