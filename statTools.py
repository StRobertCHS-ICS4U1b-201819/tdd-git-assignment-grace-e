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


"""
# Measures of Spread

#  the median of the lower half of the data set.
def lowerQuart(numList):
    '''A description of the function

     :param arg1: A description of the first argument
     :param arg2: A description of the second argument
     :return: A description of the return value
     '''


   try:
       numList.sort()
       mid = round((len(numList) + 0.1) / 2)
       return median(numList[:mid])
   except TypeError:
       return "Must be list of numbers"
   except AttributeError:
       return "This is not a list"
   except IndexError:
       return "This is an empty list"
   except:
       return "An error has occurred"

def variance(numList):
    '''
    A description of the function

     :param arg1: A description of the first argument
     :param arg2: A description of the second argument
     :return: A description of the return value
     '''
   try:
        if len(numList) == 1:
            raise TypeError
        else:
            sum = 0
            for k in range(len(numList)):
                sum += numList[k]
            numMean = sum / len(numList)
            acc2 = 0
            for i in range(len(numList)):
                acc2 += (numList[i] - numMean) ** 2
            x = acc2 / len(numList)
            rounded = "{0:0.3f}".format(x)
            return float(rounded)
    except TypeError:
        return "Must be list of numbers greater than one"
    except ZeroDivisionError:
        return "The list length is zero"
    except:
        return "An error has occurred"
"""