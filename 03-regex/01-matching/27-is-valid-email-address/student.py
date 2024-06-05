import re

def is_valid_email_address(string):
    return re.fullmatch(r'([a-zA-Z0-9]|\.)+@(ucll\.be|student\.ucll\.be)', string)