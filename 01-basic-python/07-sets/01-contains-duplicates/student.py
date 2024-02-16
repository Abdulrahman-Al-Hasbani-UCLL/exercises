# Write your code here
def contains_duplicates(xs):
    nset = set(xs)
    if len(nset) == len(xs):
        return False
    else:
        return True