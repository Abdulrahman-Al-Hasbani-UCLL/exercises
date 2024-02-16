# Write your code here
def make_path(parts):
    tekst = ''
    for item in parts:
        tekst += item +'/'
    tekst = tekst[:-1]
    return tekst
    