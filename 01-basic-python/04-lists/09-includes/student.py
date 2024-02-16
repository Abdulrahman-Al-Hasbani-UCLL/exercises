# Write your code here
def includes(xs, ys):
    for i in range(len(ys)):
        if ys[i] not in xs:
            return False
    return True