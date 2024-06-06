def movie_count(movies, director):
    return len([m for m in movies if director in m.director])

def longest_movie_runtime_with_actor(movies, actor):
    return max([m.runtime for m in movies if actor in m.actors])

def has_director_made_genre(movies, director, genre):
    return (genre in [g for m in movies if m.director == director for g in m.genres])

def is_prime(n):
    return 2==len([x for x in range(1,n+1) if n%x==0])

def is_increasing(ns:list):
    return all(x <= y for x, y in zip(ns, ns[1:]))

def count_matching(xs, ys):
    return sum(1 for x, y in zip(xs, ys) if x == y)

def weighted_sum(ns, weights):
    return sum(n * w for n, w in zip(ns, weights))


def alternating_caps(string):
    chars = [char.upper() if index % 2 == 0 else char.lower() for index, char in enumerate(string)]
    return "".join(chars)


def find_repeated_words(sentence):
    import re
    words = [word.lower() for word in re.findall('[a-zA-Z]+', sentence)]
    return {word1 for word1, word2 in zip(words, words[1:]) if word1 == word2}
