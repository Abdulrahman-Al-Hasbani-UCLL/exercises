def find(list, condition):
    
    for item in list:
        if condition(item):
            return item
    return None