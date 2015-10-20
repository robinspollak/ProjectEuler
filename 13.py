fileofnums =  open('long_nums.txt')
listofnums = []
for line in fileofnums: listofnums.append(int(line))
print(str(sum(listofnums))[0:10])