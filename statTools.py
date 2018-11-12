"""
-------------------------------------------------------------------------------
Name:		statTools.py
Purpose:
Statistical functions run on given lists
Author:		E. Shi-Shun, G. Leung
Created:		11/11/2018
------------------------------------------------------------------------------
"""

import math

# Measures of Central Tendency


def mean(numList):
    '''
    Finds the average value of all the data in the set

    :param numList: List of numbers
    :return: float The mean of the given list rounded to eight decimal places
    '''

    sum = 0
    try:
        # adds each number in the list to an accumulator
        for i in range(len(numList)):
           sum += numList[i]

        # returns the average of the numbers in the list
        return round(sum / len(numList), 8)
    except TypeError:
        return "Must enter a list of numbers"
    except ZeroDivisionError:
        return "Illegal empty list causes division error"

      
#  the middle value in a data set that has been arranged in numerical order
def median(numList):
    '''
    Find the median of a given list

    :param numList: list of ints
    :return: float median of list
    '''
    if len(numList) == 0:
        raise ValueError("Illegal empty list")

    else:
        try:
            numList.sort()
            middle = len(numList) // 2

            #if list is even then find the midpoint of the two middle numbers
            if(len(numList) % 2 == 0):
                return (numList[middle] + numList[middle - 1]) / 2

            # return the number in the middle of the ordered list
            else:
                return numList[middle]

        except TypeError:
            raise TypeError("Please provide numbers only")


def mode(numList):
    '''
    Finds the value(s) the occur most often in a given list

    :param numList: List of numbers
    :return: float The single value that occurs the most or a list of value(s) the occur equally the most
    '''
    
    occursMost = 0
    modeList = []
    try:
        for i in range(len(numList)):
            numAmount = numList.count(numList[i])

            # checks to see if a number occurs more than the previous ones
            if numAmount > occursMost:
                occursMost = numList.count(float(numList[i]))
                modeList = []
                modeList.append(float(numList[i]))

            # if there are multiple modes, it will add them to the list
            elif numAmount == occursMost and numList[i] not in modeList:
                modeList.append(float(numList[i]))

        # returns the mode or list of modes
        if len(modeList) <= 1:
            return modeList[0]
        else:
            return modeList
    except ValueError:
        return "Must enter a list of numbers"
    except:
        return "An error has occurred"


# Measures of Spread


# The exclusive range is the difference between the largest and smallest results in a data set
def range(numList):
    '''
    Find range of a given list
    :param numList: list of ints
    :return: float range of list
    '''
    
    if len(numList) == 0:
        raise ValueError("Illegal empty list")
    else:
        try:
            numList.sort()
            # return the difference between the highest and lowest number
            return numList[-1] - numList[0]
        except TypeError:
            raise TypeError("Please provide numbers only")


#  the median of the upper half of the data set.
def upperQuart(numList):
    '''
    :param numList: list of numbers
    :return: float upper quartile of list
    '''

    if len(numList) == 0:
        raise ValueError("Illegal empty list")

    else:
        try:
            numList.sort()
            # use only the last half of the list
            half = numList[len(numList) // 2:]
            # return the median of the upper half of the list
            return median(half)
          
        except TypeError:
            raise TypeError("Please provide numbers only")

          
def lowerQuart(numList):
    '''
    Finds the median for the lower half of the sorted given list

    :param numList: List of numbers
    :return: float The middle number of the lower half of a sorted list
    '''
    
    try:
        # sorts the list and finds the point to split list in half
        numList.sort()
        mid = round((len(numList) + 0.1) / 2)
        return median(numList[:mid])
    except TypeError:
        return "Must enter list of numbers"
    except AttributeError:
        return "This is not a list"
    except ValueError:
        return "Illegal empty list"
    except:
        return "An error has occurred"


def variance(numList):
    '''
    Solves the variance of a number from the mean of a given list

    :param numList: List of numbers
    :return: float The variance of the given list rounded to three decimal places
    '''
   
    try:
        # does not solve for variance if there is only one number
        if len(numList) == 1:
            raise TypeError
        else:
            # calculates the mean of the list
            sum = 0
            for i in range(len(numList)):
                sum += numList[i]
            numMean = sum / len(numList)

            # adds all the squares of the differences from the mean and stores it to an accumulator
            sumSquares = 0
            for j in range(len(numList)):
                sumSquares += (numList[j] - numMean) ** 2

            # divides the accumulator by the length of the list and rounds to three decimal places
            finalVariance = sumSquares / len(numList)
            rounded = "{0:0.3f}".format(finalVariance)
            return float(rounded)
    except TypeError:
        return "Must be list of numbers greater than one"
    except ZeroDivisionError:
        return "The list length is zero"
    except:
        return "An error has occurred"

      
def stanDev(numList):
    '''
    solve for the standard deviation of a given list

    :param numList: list of numbers
    :return: float standard deviation of list
    '''

    if len(numList) == 0:
        raise ValueError("Illegal empty list")
    else:
        try:
            mean = sum(numList) / len(numList)
            meanDiff = 0

            # find the sum of the squares of the differences between the list elements and the mean
            for i in numList:
                meanDiff += ((mean - i) ** 2)

            # return the squareroot of the mean of the total
            return round(math.sqrt(meanDiff / len(numList)), 2)
        except TypeError:
            raise TypeError("Please provide numbers only")
 
