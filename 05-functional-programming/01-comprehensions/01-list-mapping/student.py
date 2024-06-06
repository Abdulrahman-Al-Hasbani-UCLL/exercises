#import movie
#from movie import Movie

def titles(movies:list):
    return [m.title for m in movies]

def titles_and_years(movies:list):
    return [(m.title, m.year) for m in movies]

def titles_and_actor_counts(movies:list):
    return [(m.title, len(m.actors)) for m in movies]

def reverse_words(sentence:str):
    return ' '.join(word[::-1] for word in sentence.split())