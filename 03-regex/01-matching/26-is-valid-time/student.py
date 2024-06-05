import re

def is_valid_time(string):
    return re.fullmatch(r'[0-2][0-9]:[0-6][0-9]:[0-6][0-9](\.[0-9]{3})?',string)