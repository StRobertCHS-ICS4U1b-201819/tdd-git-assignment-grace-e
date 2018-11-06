import math

# Measures of Central Tendency

# the average value of all the data in the set
def mean(numList):
    sum = 0
    for i in range(len(numList)):
       sum += numList[i]
    return sum / len(numList)

#  the middle value in a data set that has been arranged in numerical order
def median(numList):
   pass

# is the value that occurs most frequently in the set
def mode(numList):
   most = 0
   for i in range(len(numList)):
       if numList.count(numList[i]) > most:
           most = numList.count(numList[i])

# Measures of Spread

# The exclusive range is the difference between the largest and smallest results in a data set
def range(numList):
   pass

#  the median of the lower half of the data set.
def lowerQuart(numList):
   pass

#  the median of the upper half of the data set.
def upperQuart(numList):
   pass

def variance(numList):
   pass

def stanDev(numList):
   pass
