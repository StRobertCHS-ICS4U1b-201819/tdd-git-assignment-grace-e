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
# median tests

def test_median_basic1():
    assert(median([2, 4, 1, 5, 9]) == 4)

def test_median_basic2():
   assert(median([2, 4, 0, 6, 1]) == 2)

def test_median_basic3():
   assert(median([2, 4, 1, 6]) == 3)

def test_median_basic4():
   assert(median([1, 2, 3, 4]) == 2.5)

def test_median_one():
   assert(median([1]) == 1)

def test_median_empty():
   with pytest.raises(ValueError) as emptyerrmsg: median([])
   assert("Illegal empty list" == str(emptyerrmsg.value))

def test_median_input():
   with pytest.raises(TypeError) as inputerrmsg: median(["no", "hi!"])
   assert("Please provide numbers only" == str(inputerrmsg.value))

#range tests

def test_range_basic1():
    assert(range([2, 4, 1, 5, 9]) == 8)

def test_range_basic2():
   assert(range([2, 4, 0, 6, 1]) == 6)

def test_range_basic3():
   assert(range([2, 7, -3, 6, 1]) == 10)

def test_range_basic4_neg():
   assert(range([-8, -3, -9, -2]) == 7)

def test_range_one():
   assert (range([1]) == 0)

def test_range_empty():
   with pytest.raises(ValueError) as emptyerrmsg: range([])
   assert("Illegal empty list" == str(emptyerrmsg.value))

def test_range_input():
    with pytest.raises(TypeError) as inputerrmsg: range(["hi", "hello", "hey"])
    assert("Please provide numbers only" == str(inputerrmsg.value))
    
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

def test_upperQuart_one():
   assert(upperQuart([1]) == 1)

def test_upperQuart_empty():
   with pytest.raises(ValueError) as emptyerrmsg: upperQuart([])
   assert("Illegal empty list" == str(emptyerrmsg.value))

def test_upperQuart_input():
   with pytest.raises(TypeError) as inputerrmsg: upperQuart(["a", "b", "c"])
   assert("Please provide numbers only" == str(inputerrmsg.value))

# standard deviation tests

def test_stanDev_basic1():
    assert(stanDev([2, 4, 7, 8, 9]) == 2.61)

def test_stanDev_basic2():
    assert(stanDev([3, 5, 8, 9, 1, 0]) == 3.35)

def test_stanDev_basic3():
    assert(stanDev([-2, -4, 6, -7, 9]) == 6.09)

def test_stanDev_one():
    assert(stanDev([10]) == 0)

def test_stanDev_empty():
    with pytest.raises(ValueError) as errmsg: stanDev([])
    assert("Illegal empty list" == str(errmsg.value))

def test_staDev_input():
    with pytest.raises(TypeError) as errmsg: stanDev(["yes", "no", "maybe"])
    assert("Please provide numbers only" == str(errmsg.value))

