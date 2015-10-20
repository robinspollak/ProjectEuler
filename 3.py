import math
all_nums = range(2,int(math.sqrt(600851475143)))
factors = filter(lambda x:600851475143%x==0,all_nums)

def recursiveSieve(mylist):
	if (len(mylist)==1): return mylist[0]
	return recursiveSieve(filter(lambda x:x%mylist[0]!=0,mylist))

print(recursiveSieve(factors))