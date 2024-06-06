def take_while(xs,condition):
    good = list()
    rest = list()

    for i in range(len(xs)):
        if condition(xs[i]) ==False:
            rest = xs[i:]
            break
        else:
            good.append(xs[i])

    return (good, rest)