import re

def is_dna(string):
    return re.fullmatch(r'(G|A|T|C)*',string)