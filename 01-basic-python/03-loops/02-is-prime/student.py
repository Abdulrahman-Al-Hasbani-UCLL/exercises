# Write your code here
def is_prime(n):
    aantal = 0
    for i in range(n):
        if n%(i+1) ==0:
            aantal+=1
    if aantal ==2:
        return True
    else:
        return False