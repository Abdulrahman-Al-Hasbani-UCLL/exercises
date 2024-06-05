import re

def is_valid_student_id(string):
    return re.fullmatch(r'(r|s|R|S)[0-9]{7}',string)