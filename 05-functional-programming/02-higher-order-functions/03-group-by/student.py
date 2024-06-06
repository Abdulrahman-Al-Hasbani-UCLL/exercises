def group_by(xs, key_function):
    result = dict()

    for item in xs:
        key = key_function(item)
        if key not in result:
            result[key]= []
        result[key].append(item)
    
    return result
