list_of_products = []
a,b=100,100
while(a<=999):
	b=100
	while(b<=999):
		list_of_products.append(a*b)
		b+=1
	a+=1
palindrome_products = filter(lambda x: (x[0:(len(x)/2)]==x[len(x)/2:][::-1])\
	,map(lambda x:str(x),list_of_products))
print max(map(lambda x:int(x),palindrome_products))	
