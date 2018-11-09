"""
-------------------------------------------------------------------------------
Name:		statTools.py
Purpose:
Statistical functions run on given lists

Author:		E. Shi-Shun, G. Leung

Created:		11/11/2018
------------------------------------------------------------------------------
"""


# Measures of Central Tendency
# add comments and docstrings after/ to refactor


#  the middle value in a data set that has been arranged in numerical order
def median(numList):
    '''
    Find the median of a given list
    :param numList: list of ints
    :return: float median of list
    '''
    
    numList.sort()
    middle = len(numList) // 2

    if(len(numList) % 2 == 0):
        return (numList[middle] + numList[middle - 1]) / 2

    else:
        return numList[middle]


# Measures of Spread

# The exclusive range is the difference between the largest and smallest results in a data set
def range(numList):
    '''
    Find range of a given list

    :param numList: list of ints
    :return: float range of list
    '''
    numList.sort()
    return numList[-1] - numList[0]


#  the median of the upper half of the data set.
def upperQuart(numList):
    numList.sort()
    mid = len(numList) // 2
    half = numList[mid:]
    quart = len(half) // 2
    return half[quart]


def stanDev(numList):
   pass


