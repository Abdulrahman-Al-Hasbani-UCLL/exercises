# Write your code here
def keys_with_value(dictionary:dict, value):
    ll = []
    for key in dictionary.keys():
        if dictionary[key] == value:
            ll.append(key)
    return ll