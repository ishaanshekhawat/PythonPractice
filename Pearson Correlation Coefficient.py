# Given two vectors, represented as lists X and Y, return the Pearson Correlation Coefficient.

# p.s. this is the same as question 9.8 in Ace the Data Science Interview.

# p.p.s. AQR is a competitive hedge fund so they test their Quants & Data Science 
# on both coding & math/stats skills, so they expect you to know the Pearson correlation coefficient formula.

import math
from functools import reduce

def corr(x, y):
	# Calculate mean of list x using reduce (sum of elements / number of elements)
	meanX = reduce(lambda x, y: x + y, x) / len(x)
	# Calculate mean of list y
	meanY = reduce(lambda x, y: x + y, y) / len(y)
	
	# Initialize variables for covariance and variances
	sigX = 0   # Sum of squared deviations for x
	sigY = 0   # Sum of squared deviations for y
	covXY = 0  # Covariance numerator accumulator
	
	# Loop over all data points
	for i in range(len(x)):
		# Increment covariance numerator
		covXY += (x[i] - meanX) * ((y[i] - meanY))
		# Increment variance components for x and y
		sigX += (x[i] - meanX) ** 2
		sigY += (y[i] - meanY) ** 2
	
	# Return Pearson correlation coefficient
	# Formula: cov(X,Y) / sqrt(var(X) * var(Y))
	return covXY / math.sqrt(sigX * sigY)
		
