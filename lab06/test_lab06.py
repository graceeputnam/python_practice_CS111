from lab06 import *
import pytest
# Remember to import from the lab06 file and pytest

# Write your test code here for Q1

def test_product():
    assert product(2) == 2
    assert product(5) == 120
    with pytest.raises(ValueError):
        product(-3)
    with pytest.raises(ValueError):
        product(1.2)



def test_summation():
    assert summation(2) == 3
    assert summation(5) == 15
    with pytest.raises(ValueError):
        summation(-3)
    with pytest.raises(ValueError):
        summation(1.2)


# Q2
#####################################

def test_square():
    assert square(2) == 4
    assert square(5) == 25


def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(9) == 3


def test_mean():
    assert mean([1, 1, 1, 3, 4]) == 2
    assert mean([3, 3, 3]) == 3
    with pytest.raises(ValueError):
        product(-3)
    with pytest.raises(ValueError):
        product(["g"])


def test_median():
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4, 5, 6]) == 3.5
    with pytest.raises(ValueError):
        product(-3)
    with pytest.raises(ValueError):
        product(["g"])


def test_mode():
    assert mode([1, 2, 1, 1]) == 1
    assert mode([1, 1, 2, 2]) == 1
    with pytest.raises(ValueError):
        product(-3)
    with pytest.raises(ValueError):
        product(["g"])


def test_std_dev():
    assert std_dev([1, 2, 3, 4, 5]) == pytest.approx(1.4142, 0.1)
    assert std_dev([1, 2, 3]) == pytest.approx(0.8165, 0.1)
    with pytest.raises(ValueError):
        product(-3)
    with pytest.raises(ValueError):
        product(["g"])


def test_stat_analysis():
    assert square(2) == 4
    assert square(5) == 25
    assert sqrt(4) == 2
    assert sqrt(9) == 3
    assert mean([1, 1, 1, 3, 4]) == 2
    assert mean([3, 3, 3]) == 3
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4, 5, 6]) == 3.5
    assert mode([1, 2, 1, 1]) == 1
    assert mode([1, 1, 2, 2]) == 1
    assert std_dev([1, 2, 3, 4, 5]) == pytest.approx(1.4142, 0.1)
    assert std_dev([1, 2, 3]) == pytest.approx(0.8165, 0.1)
    with pytest.raises(ValueError):
        product(-3)
    with pytest.raises(ValueError):
        product(["g"])

# OPTIONAL
#####################################

def test_accumulate():
    """*** YOUR CODE HERE ***"""


def test_product_short():
    """*** YOUR CODE HERE ***"""


def test_summation_short():
    """*** YOUR CODE HERE ***"""


def test_invert():
    """*** YOUR CODE HERE ***"""


def test_change():
    """*** YOUR CODE HERE ***"""


def test_invert_short():
    """*** YOUR CODE HERE ***"""


def test_change_short():
    """*** YOUR CODE HERE ***"""
