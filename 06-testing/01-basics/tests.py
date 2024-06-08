from intervals import overlapping_intervals

def test_overlapping_intervals_case1():
    assert overlapping_intervals((1, 5), (3, 6))

def test_overlapping_intervals_case2():
    assert not overlapping_intervals((2, 5), (7, 10))

def test_overlapping_intervals_case3():
    assert overlapping_intervals((-9,10), (-1,30))

def test_overlapping_intervals_case4():
    assert not overlapping_intervals((-3,5),(-9,-5))

def test_overlapping_intervals_case5():
    assert not overlapping_intervals((0,0),(1,2))

def test_overlapping_intervals_case6():
    assert not overlapping_intervals((1,0),(0,0))