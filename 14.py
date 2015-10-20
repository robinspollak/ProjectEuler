def collatz(n,our_dict):
	original = n
	counter = 0
	while True:
		if n==1: 
			our_dict[original]=counter
			return counter,our_dict
		elif n in our_dict:
			return our_dict[n]+counter,our_dict
		elif n%2 == 0:
			n = n/2
			counter+=1
		else:
			n= (3*n)+1
			counter+=1

max_length = 0
max_num = 1
memoization = {}
for number in range(500000,1000000):
	length,memoization = collatz(number,memoization)
	if length>max_length: 
		max_length=length
		max_num=number
print max_num



