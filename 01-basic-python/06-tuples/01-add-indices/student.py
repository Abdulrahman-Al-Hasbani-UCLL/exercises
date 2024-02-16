# Write your code here
def add_indices(xs):
    num = []
    for i in range(len(xs)+1):
        num.append(i) 
    return list(zip(num, xs))