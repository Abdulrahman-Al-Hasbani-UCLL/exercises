# Write your code here
def remove_duplicates(xs):
    bestaat = set()
    antwoord = []
    for element in xs:
        if element not in bestaat:
            bestaat.add(element)
            antwoord.append(element)
    return antwoord