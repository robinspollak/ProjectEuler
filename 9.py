def prob9():
	a = 3
	while True:
		for b in range(2,a):
			for c in range(1,b):
				if (pow(b,2)+pow(c,2)==pow(a,2)):
					if (a+b+c==1000):
						return a*b*c
		a+=1
print prob9()
