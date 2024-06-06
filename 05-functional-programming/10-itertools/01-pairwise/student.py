from itertools import pairwise

def total_distance(path, distance ):
    path = iter(path)
    total= 0
    for pair in list(pairwise(path)):
        total += distance(pair[0], pair[1])

    return total