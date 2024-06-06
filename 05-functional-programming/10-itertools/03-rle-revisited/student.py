import itertools

def rle_encode(data):
    return [(char, len(list(group))) for char, group in itertools.groupby(data)]

def rle_decode(data):
    return ''.join(char * count for char, count in data)