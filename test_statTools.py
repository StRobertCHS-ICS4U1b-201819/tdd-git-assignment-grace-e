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

# tests for mean function
def test_mean_uniform():
    assert mean([1, 1, 1, 1, 1]) == 1


def test_mean_basic1():
    assert mean([5, 5, 4, 54, 3, 1, 10, 7, 9, 2]) == 10


def test_mean_basic2():
    assert mean([8, 7, 6, 8, 9, 10, 12, 30, 12, 24, 50, 30, 11]) == 16.69230769


def test_mean_basic3():
    assert mean([100, 30, 20, 60, 44, 66, 55, 22, 1, 2, 3, 4]) == 33.91666667


def test_mean_float():
    assert mean([1.2, 3.4, 5.6, 7.8, 7.6, 9.1, 12.2]) == 6.7


def test_mean_basic4():
    assert mean([1.4, 50, 10000, 500, 6.6, 1.1, 3.3, 6.5]) == 1321.1125


def test_mean_negative():
    assert mean([-3, -6, -2, -4, -4.3, -10.1, 8]) == -3.05714286


def test_mean_emptyList():
    assert mean([]) == "Illegal empty list causes division error"


def test_mean_letters():
    assert mean(['h', 3, 1, 'l', 0]) == "Must enter a list of numbers"


def test_mean_variables():
    with pytest.raises(NameError):
        assert mean([e, r, i, n]) == "Variables have not been initialized"

# median tests
def test_median_basic1():
    assert(median([2, 4, 1, 5, 9]) == 4)

    
def test_median_basic2():
    assert(median([2, 4, 0, 6, 1]) == 2)

    
def test_median_basic3():
    assert(median([2, 4, 1, 6]) == 3)

    
def test_median_basic4():
    assert(median([1, 2, 3, 4]) == 2.5)

    
def test_median_basic5():
    assert(median([0.1, 0.2, 0.3, 0.4, 0.5]) == 0.3)


def test_median_basic6():
    assert(median([1000, 10, 1, 10000000]) == 505)

    
def test_median_basic6():
    assert(median([1000, 10, 1, 10000000]) == 505)

    
def test_median_one():
    assert(median([1]) == 1)

    
def test_median_empty():
    with pytest.raises(ValueError) as emptyerrmsg: median([])
    assert("Illegal empty list" == str(emptyerrmsg.value))

    
def test_median_input():
    with pytest.raises(TypeError) as inputerrmsg: median(["no", "hi!"])
    assert("Please provide numbers only" == str(inputerrmsg.value))

# tests for mode function
def test_mode_basic1():
    assert mode([8, 9, 6, 0, 4, 7, 6, 8, 8, 8, 1, 3, 3]) == 8


def test_mode_basic2():
    assert mode([9, 8, 9, 9, 7, 9, 6, 9, 5, 0, 3, 9, 6, 8]) == 9


def test_mode_basic3():
    assert mode([1, 1, 2, 3, 4, 4, 4]) == 4


def test_mode_basic4():
    assert mode([-1, -2, -1, -2, -2, 3, 3, 9]) == -2


def test_mode_single():
    assert mode([8]) == 8


def test_mode_noList():
    assert mode(8) == "An error has occurred"


def test_mode_empty():
    assert mode([]) == "An error has occurred"


def test_mode_letters():
    assert mode(['h', 'i']) == "Must enter a list of numbers"


def test_mode_variables():
    with pytest.raises(NameError):
        assert mode([e, n]) == "Variables have not been initialized"


def test_multiple_modes():
    assert mode([0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 9, 10, 11, 12, 12, 12]) == [2, 3, 4, 12]

#range tests
def test_range_basic1():
    assert(range([2, 4, 1, 5, 9]) == 8)

    
def test_range_basic2():
    assert(range([2, 4, 0, 6, 1]) == 6)

    
def test_range_basic3():
    assert(range([2, 7, -3, 6, 1]) == 10)

    
def test_range_basic4_neg():
    assert(range([-8, -3, -9, -2]) == 7)

    
def test_range_basic5():
    assert(range([0.00001, 0.0003, 0.0002, 1.00001]) == 1)


def test_range_basic6():
    assert(range([10000000000, 5554, 123, 0]) == 10000000000)

    
def test_range_one():
    assert (range([1]) == 0)

    
def test_range_empty():
    with pytest.raises(ValueError) as emptyerrmsg: range([])
    assert("Illegal empty list" == str(emptyerrmsg.value))

    
def test_range_input():
    with pytest.raises(TypeError) as inputerrmsg: range(["hi", "hello", "hey"])
    assert("Please provide numbers only" == str(inputerrmsg.value))

# tests for lower quartile function
def test_lowerQuart_basic1():
    assert lowerQuart([1, 2, 3, 4, 4, 5, 20, 30, 40, 43]) == 3


def test_lowerQuart_basic2():
    assert lowerQuart([1, 65, 67, 20, 4, 5, 68, 30, 40, 55, 43, 4, 2]) == 4


def test_lowerQuart_basic3():
    assert lowerQuart([1, 2, 3, 4]) == 1.5


def test_lowerQuart_basic4():
    assert lowerQuart([8, 2.5, 3.25, 7.4, 9, 1, 99]) == 2.875


def test_lowerQuart_duel():
    assert lowerQuart([1, 2]) == 1


def test_lowerQuart_single():
    assert lowerQuart([9]) == 9


def test_lowerQuart_number():
    assert lowerQuart(8) == "This is not a list"


def test_lowerQuart_empty():
    assert lowerQuart([]) == "Illegal empty list"


def test_lowerQuart_letters():
    assert lowerQuart(['h', 'e', 'y', 'o']) == "Must enter list of numbers"

    
def test_lowerQuart_variables():
    with pytest.raises(NameError):
        assert lowerQuart([l, q]) == "Variables have not been initialized"

    
# upper quartile tests
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

    
def test_upperQuart_basic6():
    assert(upperQuart([0.2, 4, 1, 6000200, 5]) == 5)

    
def test_upperQuart_one():
    assert(upperQuart([1]) == 1)

    
def test_upperQuart_empty():
    with pytest.raises(ValueError) as emptyerrmsg: upperQuart([])
    assert("Illegal empty list" == str(emptyerrmsg.value))

    
def test_upperQuart_input():
    with pytest.raises(TypeError) as inputerrmsg: upperQuart(["a", "b", "c"])
    assert("Please provide numbers only" == str(inputerrmsg.value))
 

# tests for variance function
def test_variance_basic1():
    assert variance([3, 4, 5, 5, 6, 7, 9]) == 3.388

    
def test_variance_basic2():
    assert variance([0, 4, 4, 7, 7, 7, 8, 8, 8, 9, 9, 11, 11, 11]) == 8.816


def test_variance_negative():
    assert variance([-117, -4.5, -3, -3, -2.9, -1, 2, 99]) == 2928.267
 

def test_variance_basic3():
    assert variance([1, 2, 3, 10]) == 12.5

    
def test_variance_basic4():
    assert variance([1, 50000]) == 624975000.25


def test_variance_uniform():
    assert variance([8, 8, 8, 8, 8, 8]) == 0


def test_variance_single():
    assert variance([3]) == "Must be list of numbers greater than one"


def test_variance_empty():
    assert variance([]) == "The list length is zero"

    
def test_variance_letters():
    assert variance(['h', 'e', 'n', 'y', 'l', 'o']) == "Must be list of numbers greater than one"

    
def test_variance_variables():
    with pytest.raises(NameError):
        assert variance([d, _]) == "Variables have not been initialized"

# standard deviation tests
def test_stanDev_basic1():
    assert(stanDev([2, 4, 7, 8, 9]) == 2.61)

    
def test_stanDev_basic2():
    assert(stanDev([3, 5, 8, 9, 1, 0]) == 3.35)


def test_stanDev_basic3():
    assert(stanDev([-2, -4, 6, -7, 9]) == 6.09)
    
    
def test_stanDev_basic4():
    assert(stanDev([1100, 2323232323, 9, 0.2, 6, 5, 799]) == 812961851.68)


def test_stanDev_basic3():
    assert(stanDev([1100, 2323232323, 9, 0.2, 6, 5, 799]) == 812961851.68)

def test_stanDev_one():
    assert(stanDev([10]) == 0)


def test_stanDev_empty():
    with pytest.raises(ValueError) as errmsg: stanDev([])
    assert("Illegal empty list" == str(errmsg.value))


def test_staDev_input():
    with pytest.raises(TypeError) as errmsg: stanDev(["yes", "no", "maybe"])
    assert("Please provide numbers only" == str(errmsg.value))

