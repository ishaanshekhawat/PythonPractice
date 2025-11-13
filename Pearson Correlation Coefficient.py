# Given two vectors, represented as lists X and Y, return the Pearson Correlation Coefficient.

# p.s. this is the same as question 9.8 in Ace the Data Science Interview.

# p.p.s. AQR is a competitive hedge fund so they test their Quants & Data Science 
# on both coding & math/stats skills, so they expect you to know the Pearson correlation coefficient formula.

import math
from functools import reduce

def corr(x, y):
	meanX = reduce(lambda x,y:x+y, x)/len(x)
	meanY = reduce(lambda x,y:x+y, y)/len(y)
	sigX = 0
	sigY = 0
	covXY = 0
	for i in range(len(x)):
		covXY += (x[i]-meanX)*((y[i]-meanY))
		sigX += (x[i]-meanX)**2
		sigY += (y[i]-meanY)**2
	return covXY/math.sqrt(sigX*sigY)
		