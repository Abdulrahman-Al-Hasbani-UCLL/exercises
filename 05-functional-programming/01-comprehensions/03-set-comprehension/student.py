def directors(movies):
    return {m.director for m in movies}

def common_elements(xs, ys):
    return {value for value in xs if value in ys}