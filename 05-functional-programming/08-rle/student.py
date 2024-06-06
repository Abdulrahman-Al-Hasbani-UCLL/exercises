def rle_encode(data):
    data = iter(data)
    try:
        last_char = next(data)
        count = 1
        for char in data:
            if last_char == char:
                count += 1
            else:
                yield (last_char, count)
                last_char = char
                count = 1
        yield (last_char, count)
    except StopIteration:
        pass

def rle_decode(data):
    for char, count in data:
        for _ in range(count):
            yield char
