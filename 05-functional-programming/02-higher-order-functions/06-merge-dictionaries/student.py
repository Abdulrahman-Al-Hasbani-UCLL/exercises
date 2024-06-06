def merge_dictionaries(d1:dict, d2:dict, merge_function):
    result = dict()

    for key in d1.keys():
        if key not in d2.keys():
            result[key] = d1[key]
        else:
            result[key] = merge_function(d1[key], d2[key])

    for key in d2.keys():
        if key not in result.keys():
            result[key] = d2[key]
    
    return result
            