import re

def starts_with_a(string):
    return re.search(r'^a', string)  