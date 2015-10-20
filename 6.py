list_of_nums = range(0,101)
sum_of_squares = sum(map(lambda x:pow(x,2),list_of_nums))
square_of_sum = pow(sum(list_of_nums),2)
print (square_of_sum - sum_of_squares)