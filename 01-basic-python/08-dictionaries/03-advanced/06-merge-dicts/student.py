# Write your code here
def merge_dicts(dictionary1:dict, dictionary2:dict):
    ndict = dict()
    for key in dictionary1:
        ndict[key] = dictionary1[key]
    for key in dictionary2:
        ndict[key] = dictionary2[key]

    return ndict