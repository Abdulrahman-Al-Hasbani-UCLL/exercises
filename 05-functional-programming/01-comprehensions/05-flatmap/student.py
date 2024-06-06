from util import Card

def genres(movies):
    return {g for m in movies for g in m.genres}

def actors(movies):
    return {a for m in movies for a in m.actors}

def repeat_consecutive(xs, n):
    return [x for x in xs for repeat in range(n)]

def repeat_alternating(xs, n):
    return [x for _ in range(n) for x in xs]

def cards(values, suits):
    return {Card(x, s) for x in values for s in suits}