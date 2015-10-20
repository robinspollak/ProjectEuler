def divisors(n):
    if n % 2 == 0: n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors

n=1
lfactors,rfactors = divisors(n),divisors(n+1)
while lfactors*rfactors<500:
	n+=1
	lfactors,rfactors = rfactors,divisors(n+1)
print ((n*(n+1))/2)
