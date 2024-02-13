# Write your code here
def median(ns):
    ns.sort()
    list_length = len(ns)
    if list_length %2 == 0:
        return float(((ns[((list_length//2)-1)]+ns[(list_length//2)])/2))
    else:
        return ns[list_length//2]