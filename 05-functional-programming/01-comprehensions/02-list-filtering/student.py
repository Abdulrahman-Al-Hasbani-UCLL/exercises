def movies_from_year(movies, year):
    return [m.title for m in movies if m.year == year]

def movies_with_actor(movies, actor):
    return [m.title for m in movies if actor in m.actors]

def divisors(n):
    return [x for x in range(1,n+1) if n%x == 0]