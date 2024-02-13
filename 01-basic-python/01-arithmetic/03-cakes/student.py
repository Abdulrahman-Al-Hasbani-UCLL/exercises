# Write your code here
def cakes(eggs:int, butter:int, flour:int):
    amount = []
    amount.append(eggs//5)
    amount.append(butter//250)
    amount.append(flour//5)

    amount.sort()
    return amount[0]