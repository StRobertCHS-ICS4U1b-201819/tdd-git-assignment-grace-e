# Video must show red-green-blue parts, git commits are in present tense, fill out the column, want some tests to fail
# commit after every test
# Measures of Central Tendency

# the average value of all the data in the set
def mean(numList):
    try:
        sum = 0
        for i in range(len(numList)):
           sum += numList[i]
        return sum / len(numList)
    except TypeError:
        return "Must be list of numbers"
    except:
        return "An error has occurred"


def median(numList):
    '''
    Find the median of a given list
    :param numList: list of ints
    :return: float median of list
    '''

    numList.sort()
    middle = len(numList) // 2

    if (len(numList) % 2 == 0):
        return (numList[middle] + numList[middle - 1]) / 2
    else:
        return numList[middle]

# is the value that occurs most frequently in the set
def mode(numList):
   try:
       y = 0
       most = []
       for i in range(len(numList)):
            if numList.count(numList[i]) > y:
                y = numList.count(float(numList[i]))
                most = []
                most.append(float(numList[i]))
            elif numList.count(numList[i]) == y and numList[i] not in most:
                most.append(float(numList[i]))
       if len(most) <= 1:
           return most[0]
       else:
           return "There are multiple modes"
   except ValueError:
       return "Must be list of numbers"
   except:
       return "An error has occurred"

# Measures of Spread

#  the median of the lower half of the data set.
def lowerQuart(numList):
   try:
       numList.sort()
       mid = round((len(numList) / 2))
       return median(numList[:mid])
   except TypeError:
       return "Must be list of numbers"
   except:
       return "An error has occurred"

def variance(numList):
    try:
        acc2 = 0
        numMean = mean(numList)
        for i in range(len(numList)):
            acc2 += (numList[i] - numMean) ** 2
        x = acc2 / len(numList)
        rounded = "{0:0.3f}".format(x)
        return float(rounded)
    except TypeError:
        return "Must be list of numbers"
    except:
        return "An error has occurred"
