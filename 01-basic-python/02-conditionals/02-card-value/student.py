# Write your code here
def card_value(kaart):
    if kaart == "Jack":
        return 11
    elif kaart == "Queen":
        return 12
    elif kaart == "King":
        return 13
    elif kaart == "Ace":
        return 1
    else:
        return int(kaart)
