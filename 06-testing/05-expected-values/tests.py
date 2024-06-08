import pytest
from mergesort import *

@pytest.mark.parametrize(('l1'), [
    list(range(x)) for x in range(101) 
])

def test_split_in_two(l1):
    left, right = split_in_two(l1)
    acu = left + right

    assert len(acu) == len(l1)
    assert abs(len(left) - len(right)) <= 1
    assert acu == l1

@pytest.mark.parametrize(('l2', 'l3'), [
    ([], []),
])

def test_merge_sorted(l2, l3):
    pass