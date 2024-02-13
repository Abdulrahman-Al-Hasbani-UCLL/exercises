# Write your code here
def coins(one, two, five, goal):
    one_true = False
    for i in range(one+1):
        for j in range(two+1):
            for k in range(five+1):
                if (i*1)+(j*2)+(k*5) == goal:
                    one_true = True
    return one_true