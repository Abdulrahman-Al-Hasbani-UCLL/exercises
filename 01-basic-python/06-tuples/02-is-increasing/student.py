# Write your code here
def is_increasing(ns):
    ms = ns[1:]
    nlist = list(zip(ns, ms))
    for i,j in nlist:
        if i>j:
            return False
    return True