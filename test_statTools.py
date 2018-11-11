"""
-------------------------------------------------------------------------------
Name:		test_statTools.py
Purpose:
test statistical functions from statTools.py

Author:		E. Shi-Shun, G. Leung

Created:		11/11/2018
------------------------------------------------------------------------------
"""

import pytest
from statTools import *

def test_median_basic1():
    assert(median([2, 4, 1, 5, 9]) == 4)

def test_median_basic2():
   assert(median([2, 4, 0, 6, 1]) == 2)

def test_median_basic3():
   assert(median([2, 4, 1, 6]) == 3)

def test_median_basic4():
   assert(median([1, 2, 3, 4]) == 2.5)

def test_median_empty():
   with pytest.raises(ValueError) as emptyerrmsg: median([])
   assert ("Illegal empty list" == str(emptyerrmsg.value))

def test_median_input():
   with pytest.raises(TypeError) as inputerrmsg: median(["no", "hi!"])
   assert ("Please provide numbers only" == str(inputerrmsg.value))



def test_range_basic1():
    assert(range([2, 4, 1, 5, 9]) == 8)

def test_range_basic2():
   assert(range([2, 4, 0, 6, 1]) == 6)

def test_range_basic3():
   assert(range([2, 7, -3, 6, 1]) == 10)

def test_range_basic4_neg():
   assert(range([-8, -3, -9, -2]) == 7)

def test_range_empty():
   with pytest.raises(ValueError) as emptyerrmsg: range([])
   assert ("Illegal empty list" == str(emptyerrmsg.value))

def test_range_input():
    with pytest.raises(TypeError) as inputerrmsg: range(["hi", "hello", "hey"])
    assert("Please provide numbers only" == str(inputerrmsg.value))
    
    

def test_upperQuart_basic1():
    assert(upperQuart([2, 4, 1, 5, 9]) == 5)

def test_upperQuart_basic2():
   assert(upperQuart([2, 4, 0, 6, 1]) == 4)

def test_upperQuart_basic3():
   assert(upperQuart([2, 4, 1, 6, 0, 7]) == 6)

def test_upperQuart_basic4():
   assert(upperQuart([3, 4, 1, 7, 8, 6]) == 7)

def test_upperQuart_basic5():
   assert(upperQuart([2, 4, 1, 6]) == 5)

def test_upperQuart_empty():
   with pytest.raises(ValueError) as emptyerrmsg: upperQuart([])
   assert ("Illegal empty list" == str(emptyerrmsg.value))

def test_upperQuart_input():
   with pytest.raises(TypeError) as inputerrmsg: upperQuart(["a", "b", "c"])
   assert ("Please provide numbers only" == str(inputerrmsg.value))

def test_mean1():
    assert(mean([1, 1, 1, 1, 1]) == 1)


def test_mean2():
    assert(mean([5, 5, 4, 54, 3, 1, 10, 7, 9, 2]) == 10)


def test_mean_emptyList():
    assert(mean([]) == "An error has occurred")


def test_mean_letters():
    assert(mean(['h', 'e', 'l', 'l', 'o']) == "Must be list of numbers")


def test_mean_variable():
    with pytest.raises(NameError):
        assert(mean([e, r, i, n]) == "Variables have not been initialized")


def test_mode1():
    assert(mode([8, 9, 6, 0, 4, 7, 6, 8, 8, 8, 1, 3, 3]) == 8)


def test_mode2():
    assert(mode([9, 8, 9, 9, 7, 9, 6, 9, 5, 0, 3, 9, 6, 8]) == 9)


def test_lowerQuart1():
    assert(lowerQuart([1, 2, 3, 4, 4, 5, 20, 30, 40, 43]) == 3)


def test_lowerQuart2():
    assert(lowerQuart([1,65, 67, 20, 4, 5, 68, 30, 40, 55, 43, 4, 2]) == 4)


def test_variance1():
    assert(variance([3, 4, 5, 5, 6, 7, 9]) == 3.388)

def test_variance2():
    assert(variance([0,4,4,7,7,7,8,8,8,9,9,11,11,11]) == 8.816)





