# https://datalemur.com/questions/python-maximum-product-three-numbers

def max_three(input):
	maxi = 0
	
	for i in range(0, len(input) - 2):
	  for j in range(i+1, len(input) - 1):
	    for k in range(j+1, len(input)):
	      if input[i]*input[j]*input[k] > maxi:
	        maxi = input[i]*input[j]*input[k]
	        print(input[i], input[j], input[k])
	
	return maxi
