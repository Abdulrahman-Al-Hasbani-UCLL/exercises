# Write your code here
def target_sum(ns:list, target):
    for i in range(len(ns)):
        for j in range(len(ns)):
            if ns[i]+ns[j] == target:
                return True
    return False