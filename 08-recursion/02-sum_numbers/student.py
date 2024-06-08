'''
def sum_numbers(n):
    n = str(n)
    s = 0
    for x in n:
        if x.isdigit():
            s+=int(x)
    
    return s
''' 
#this is the recursive

def sum_numbers(n):
    n = abs(n)

    if n < 10:
        return n
    
    return (n % 10) + sum_numbers(n // 10)