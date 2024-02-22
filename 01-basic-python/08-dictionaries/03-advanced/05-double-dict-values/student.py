# Write your code here
def double_dict_values(dictionary:dict):
    ndict = dict()
    for key in dictionary.keys():
        ndict[key] = (dictionary[key])*2
    return ndict