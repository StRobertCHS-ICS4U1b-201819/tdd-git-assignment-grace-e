# Video must show red-green-blue parts, git commits are in present tense, fill out the coloumn

import math

# Measures of Central Tendency

# the average value of all the data in the set
def mean(numList):
    sum = 0
    for i in range(len(numList)):
       sum += numList[i]
    return sum / len(numList)

# is the value that occurs most frequently in the set
def mode(numList):
   most = 0
   for i in range(len([numList])):
        if numList.count(numList[i]) > most:
            most = numList[i]
   return most

# Measures of Spread

#  the median of the lower half of the data set.
def lowerQuart(numList):
   numList = sorted(numList)
   mid = (len(numList) // 2) // 2
   return numList[mid]

def variance(numList):
    acc2 = 0
    numMean = mean(numList)
    for i in range(len(numList)):
        acc2 += (numList[i] - numMean) ** 2
    x = acc2 / len(numList)
    rounded = "{0:0.3f}".format(x)
    return float(rounded)
