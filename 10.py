import math
def is_prime(x):
	if x == 1: return False
	elif x == 2: return True
	for number in range(2,int(math.ceil(math.sqrt(x)))+1):
		if x%number == 0: return False 
	return True
print sum(filter(is_prime,range(2000000)))