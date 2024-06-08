import pytest
from mystatistics import average

@pytest.mark.parametrize(('list1', 'expected1'), [
    ([0.1,0.1,0.1], 0.1),
    ([1,1,1], 1),
    ([50, 10, 40], 33.3)
])

def test_average_is_correct(list1:list, expected1 ):
    assert pytest.approx(expected1, abs=0.1) == average(list1), f'The average of: {list1} \n should be {expected1}'

