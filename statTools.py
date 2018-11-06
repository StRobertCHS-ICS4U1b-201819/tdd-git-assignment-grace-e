# Measures of Central Tendency
# add comments and docstrings after/ to refactor

# the average value of all the data in the set
def mean(numList):
   pass

#  the middle value in a data set that has been arranged in numerical order
def median(numList):
   numList.sort()
   middle = len(numList) // 2
   if (len(numList) % 2 == 0):
       return (numList[middle] + numList[middle - 1]) / 2

   else:
      med = numList[middle]

   return med

# is the value that occurs most frequently in the set
def mode(numList):
   pass

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


