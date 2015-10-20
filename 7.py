import math
def is_prime(x):
	if x == 1: return False
	elif x == 2: return True
	for number in range(2,int(math.ceil(math.sqrt(x)))+1):
		if x%number == 0: return False 
	return True
number_primes = 1
current_number = 1
while number_primes!=10001:
	current_number+=2
	if is_prime(current_number): 
		number_primes+=1
print(current_number)