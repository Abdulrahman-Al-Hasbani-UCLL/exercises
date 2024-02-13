# Write your code here
def last_digit(num):
    return num%10
    
def remove_last_digit(num):
    return num //10
    
def digit_sum(num):
    som = 0
    n = num
    for i in range(len(str(num))):
        som+= last_digit(n)
        n = remove_last_digit(n)
    return som