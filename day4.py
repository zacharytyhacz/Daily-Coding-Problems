#Given an array of integers, find the first missing positive integer in linear time 
# and constant space. In other words, find the lowest positive integer that 
# does not exist in the array. The array can contain duplicates and negative numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.


# sort array to get lowest number 
# loop through numbers in for loop
	# if number[i] + 1 = number[i+1]
		# good 
	# else
		# x = number[i+1] - number[i]
		# for j in x
			# if number + j > 0 
				# append array with missing integers

# if missing integers array is empty, get last index + 1 


#input = [3, 4, -1 , 1]
#input = [1, 2, 0]
input = [-2,-1,0, 2, 4]
missing = []
input = sorted(input)
print(input)
for x in range(len(input)):
	if x != len(input) - 1:
		if input[x] + 1 != input[x+1]:
			for y in range(input[x]+1,input[x+1]):
				if y > 0:
					missing += [y]
	elif len(missing) == 0:
		if input[x]+1 < 0:
			missing += [1]
		else:
			missing += [input[x]+1]
print(missing)

					 
