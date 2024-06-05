import re

def parse_time(string):
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})\.{0,1}(\d{3})?', string)
    if match:
        h,m,s,ms = map(int,match.groups('000'))
        return (h,m,s,ms)