import pytest
from statTools import *

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