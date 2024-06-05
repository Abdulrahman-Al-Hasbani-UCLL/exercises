import re

def is_number(string):
    return re.fullmatch(r'[0-9]+(\.{0,1}[0-9]+)?', string)