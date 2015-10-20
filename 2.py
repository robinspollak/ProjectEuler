def fibonacci():
	a,b = 0,1
	while True:
		yield b
		a,b = b,a+b

fib_seq = fibonacci()

result =0
while True:
	working = fib_seq.next()
	if (working>4000000): break
	if (working%2==0): result+=working
print result

