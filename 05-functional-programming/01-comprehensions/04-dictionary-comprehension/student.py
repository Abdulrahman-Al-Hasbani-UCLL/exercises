def title_to_director(movies):
    return {m.title:m.director for m in movies}

def director_to_titles(movies):
    return {director:[m.title for m in movies if m.director == director] 
            for director in {m.director for m in movies}}