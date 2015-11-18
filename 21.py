def divisors(n):
	res = 0
	for div in range(1,n):
		if n%div==0: res+=div
	return res

d_list = map(lambda x:divisors(x),range(1,10000))

amicable_nums = []

for a in range(10000):
	b = d_list[a-1]
	if not b>10000:
		if d_list[b-1]==a:
			if (a!=b):
				amicable_nums.append(a)
				amicable_nums.append(b)

print amicable_nums
print sum(amicable_nums)/2

#print(sum(amicable_nums))

