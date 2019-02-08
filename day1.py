#This problem was recently asked by Google.
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
def main():
	numbers = [10,15,3,7,11,6,16,1]
	k = 17;

	for i in numbers:
		for j in numbers:
			if i + j == k:
				print(str(j) + " + " + str(i) + " == " + str(k))

main()	
