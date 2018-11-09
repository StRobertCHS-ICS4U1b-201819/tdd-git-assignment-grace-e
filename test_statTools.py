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


def test_range_basic1():
    assert(range([2, 4, 1, 5, 9]) == 8)

def test_range_basic2():
   assert(range([2, 4, 0, 6, 1]) == 6)

def test_range_basic3():
   assert(range([2, 7, -3, 6, 1]) == 10)

def test_range_basic4_neg():
   assert(range([-8, -3, -9, -2]) == 7)

def test_upperQuart_basic1():
    assert(upperQuart([2, 4, 1, 5, 9]) == 5)

def test_upperQuart_basic2():
   assert(upperQuart([2, 4, 0, 6, 1]) == 4)






