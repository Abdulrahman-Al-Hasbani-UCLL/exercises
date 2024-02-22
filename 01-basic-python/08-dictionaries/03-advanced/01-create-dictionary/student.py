# Write your code here
def create_dictionary(keys, values):
    dictionary = dict()
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]

    return dictionary