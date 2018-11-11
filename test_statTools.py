import pytest
from statTools import *

def test_mean1():
    assert(mean([1, 1, 1, 1, 1]) == 1)

def test_mean2():
    assert(mean([5, 5, 4, 54, 3, 1, 10, 7, 9, 2]) == 10)

def test_mean3():
    assert(mean([8, 7, 6, 8, 9, 10, 12, 30, 12, 24, 50, 30, 11]) == 16.69231)

def test_mean4():
    assert(mean([100, 30, 20, 60, 44, 66, 55, 22, 1, 2, 3, 4]) == 33.91667)

def test_mean5():
    assert(mean([1.2, 3.4, 5.6, 7.8, 7.6, 9.1, 12.2]) == 6.7)

def test_mean6():
    assert(mean([1.4, 50, 10000, 500, 6.6, 1.1, 3.3, 6.5]) == 1321.1125)

def test_mean_negative():
    assert(mean([-3, -6, -2, -4, -4.3, -10.1, 8]) == -3.05714 )

def test_mean_emptyList():
    assert(mean([]) == "The list length is zero")

def test_mean_letters():
    assert(mean(['h', 3, 1, 2, 0]) == "Must be list of numbers")

def test_mean_variable():
    with pytest.raises(NameError):
        assert(mean([e, r, i, n]) == "Variables have not been initialized")

def test_mode1():
    assert(mode([8, 9, 6, 0, 4, 7, 6, 8, 8, 8, 1, 3, 3]) == 8)

def test_mode2():
    assert(mode([9, 8, 9, 9, 7, 9, 6, 9, 5, 0, 3, 9, 6, 8]) == 9)

def test_mode3():
    assert(mode([1, 1, 2, 3, 4, 4, 4]) == 4)

def test_mode4():
    assert(mode([-1, -2, -1, -2, -2, 3, 3, 9]) == -2)

def test_modeSingle():
    assert(mode([8]) == 8)

def test_mode_noList():
    assert(mode(8) == "An error has occurred")

def test_mode_empty():
    assert(mode([]) == "An error has occurred")

def test_mode_letters():
    assert(mode(['h', 'i']) == "Must be list of numbers")

def test_mode_variable():
    with pytest.raises(NameError):
        assert(mode([e, n]) == "Variables have not been initialized")

def test_more_than_one_modes():
    assert(mode([0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 9, 10, 11, 12, 12, 12]) == "There are multiple modes")

def test_lowerQuart1():
    assert(lowerQuart([1, 2, 3, 4, 4, 5, 20, 30, 40, 43]) == 3)

def test_lowerQuart2():
    assert(lowerQuart([1, 65, 67, 20, 4, 5, 68, 30, 40, 55, 43, 4, 2]) == 4)

def test_lowerQuart3():
    assert(lowerQuart([1, 2, 3, 4]) == 1.5)

def test_lowerQuart_empty():
    assert(lowerQuart([]) == "An error has occurred")

def test_lowerQuart_letters():
    assert(lowerQuart(['h', 'e', 'y', 'o']) == "Must be list of numbers")

def test_lowerQuart_variable():
    with pytest.raises(NameError):
        assert(lowerQuart([l, q]) == "Variables have not been initialized")

def test_variance1():
    assert(variance([3, 4, 5, 5, 6, 7, 9]) == 3.388)

def test_variance2():
    assert(variance([0, 4, 4, 7, 7, 7, 8, 8, 8, 9, 9, 11, 11, 11]) == 8.816)

def test_variance_empty():
    assert(variance([]) == "The list length is zero")

def test_variance_letters():
    assert(variance(['h', 'e', 'n', 'y', 'l', 'o']) == "Must be list of numbers")

def test_variance_variable():
    with pytest.raises(NameError):
        assert(variance([d, _]) == "Variables have not been initialized")

