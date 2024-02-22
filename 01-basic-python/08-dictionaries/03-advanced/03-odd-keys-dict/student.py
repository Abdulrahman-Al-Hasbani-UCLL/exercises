# Write your code here
def odd_keys_dict(dictionary:dict):
    ndict = dict()
    for key in dictionary:
        if key%2 == 0:
            pass
        else:
            ndict[key] = dictionary[key]
    
    return ndict