def divisible(num):
	for divisor in range(1,21):
		if (num % divisor!=0):
			return False
	return True
result = 20
while not (divisible(result)): result+=20
print result
