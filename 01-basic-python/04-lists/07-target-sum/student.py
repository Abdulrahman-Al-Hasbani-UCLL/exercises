# Write your code here
def target_sum(lijst:list, goal):
    for i in range(len(lijst)):
        if lijst[i]+lijst[i+1]:
            return True
    return False