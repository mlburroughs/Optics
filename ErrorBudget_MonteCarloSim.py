"""
This program uses Gaussian distribution to compute error budgets based on confidence values

This program takes in 3 parameters:
confidence (array): desired range of variable for which 95% of values lie within
avg (array): Center of which the guassian distrubtion lies, for this program I use an array of 0's
numrep (int): Number of times variable is computed for guassian distribution

And outputs:
varray (array): a simulation array [i] of guassian distributions for each confidence [i]
sigma (array): RSS error for each [i] simulation

Author: Michelle Burroughs
Date 1/2/21

"""
#imports
import numpy
import math

# confidence array -> this represents the desired range of each individual parameter
# for instance, a confidence value of 2 represents a range of [-2 2] for which 95% of values lie in range
varrayc = [2, 2, 2]
sigma = [0]*len(varrayc)
# sigma = confidence/2 -> represents 95% 2*sigma
avg = [0]*len(varrayc)

for i in range(len(varrayc)):
    sigma[i] = varrayc[i]/2

numreps = 100000

# creates 2d array with rows as individual sigmas
varray = [[0]*numreps]*len(sigma)

# for each confidence interval, random values are computed
#avg is centered at 0, sigma is the confidence, and numreps is the number of times random values are computed
for i in range(len(varray)):
    varray[i] = numpy.random.normal(avg[i], sigma[i], numreps).round(3)


# computes RSS for each respective elements, resulting in numreps*results
sig2 = [0]*numreps

for i in range(numreps):
    for j in range(len(sigma)):
        sig2[i] += (varray[j][i]) * (varray[j][i])

sig = [0]*numreps
for i in range(len(sig2)):
    sig[i] = math.sqrt(sig2[i])

sig.sort()

counter = 0
for i in range(len(sig)):
    if sig[i] <= 2:
        counter += 1

percentage = (counter/len(sig))*100
print(percentage)

# Total Error Budget evaluations
print('Max sigma is: ')
print(max(sig))

print('Min sigma is: ')
print(min(sig))

print('Avg sigma is: ')
print(sum(sig)/len(sig))
