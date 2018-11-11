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
    Find the upper quartile of a given list

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

