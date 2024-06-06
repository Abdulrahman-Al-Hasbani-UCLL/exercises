def group_movies_by_year(movies):
    return {y:[m.title for m in movies if m.year == y] 
            for y in {m.year for m in movies}}