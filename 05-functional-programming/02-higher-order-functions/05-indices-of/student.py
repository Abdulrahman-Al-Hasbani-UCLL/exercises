def indices_of(xs, condition):
    good = list()

    for i in range(len(xs)):
        if condition(xs[i]):
            good.append(i)
    
    return good