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

"""
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
    '''A description of the function

     :param arg1: A description of the first argument
     :param arg2: A description of the second argument
     :return: A description of the return value
     '''

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
           return most
   except ValueError:
       return "Must be list of numbers"
   except:
       return "An error has occurred"

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