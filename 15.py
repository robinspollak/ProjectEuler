def recursive_grid(rows,cols):
	if (rows==0 and cols==0):
		return 1
	calls = 0
	if rows>0:
		calls += recursive_grid(rows-1,cols)
	if cols>0:
		calls += recursive_grid(rows,cols-1)

	return calls
print(recursive_grid(20,20))

# too slow :(