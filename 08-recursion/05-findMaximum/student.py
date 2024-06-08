def findMaximum(list):
    if not list:
        raise IndexError
    
    if len(list) == 1:
        return list[0]
    else:
        max_of_rest = findMaximum(list[1:])
        return list[0] if list[0] > max_of_rest else max_of_rest
