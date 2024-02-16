# Write your code here
def drop_nth(xs, n):
    nxs = xs[:n] + xs[n+1:]
    return nxs