# Given a list of integers, return the maximum product of any three numbers in the array.

# For example, for A = [1, 3, 4, 5], you should return 60, since 3*4*5=60.

# For B = [−4, −2, 3, 5] you should return 40 since -4*−2*5=40

def max_three(input):
	dict1 = {}
	for i in range(len(input)-2):
		for j in range(i+1, len(input)-1):
			for k in range(j+1, len(input)):
				dict1[str(i)+str(j)+str(k)] = input[i]*input[j]*input[k]
	dict2 = dict(sorted(dict1.items(), key = lambda x: x[1], reverse=True))
	for i in dict2.items():
		return i[1]
	
print(max_three([-4, -2, 3, 5]))
