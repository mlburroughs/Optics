"""
This program uses Gaussian distribution to compute error budgets based on confidence values

Author: Michelle Burroughs
Date 1/2/21

"""
#imports
import numpy
import math

# confidence array
varrayc = [3, 1, 2]
sigma = [0]*len(varrayc)
# sigma = confidence/2 -> represents 95% 2*sigma
avg = [0]*len(varrayc)

for i in range(len(varrayc)):
    sigma[i] = varrayc[i]/2

numreps = 5

# creates 2d array with rows as individual sigmas
varray = [[0]*numreps]*len(sigma)

# for each confidence interval, random values are computed
for i in range(len(varray)):
    varray[i] = numpy.random.normal(avg[i], sigma[i], numreps).round(3)


# computes RMS for each respective elements, resulting in numreps*results
sig2 = [0]*numreps

for i in range(numreps):
    for j in range(len(sigma)):
        sig2[i] += (varray[j][i]) * (varray[j][i])

sig = [0]*numreps
for i in range(len(sig2)):
    sig[i] = math.sqrt(sig2[i])

