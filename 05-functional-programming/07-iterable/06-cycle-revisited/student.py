def cycle(xs):
    index = 0
    while True:
        if index == len(xs):
            index = 0
        yield xs[index]
        index+=1
