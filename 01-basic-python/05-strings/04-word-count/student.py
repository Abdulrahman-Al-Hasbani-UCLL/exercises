# Write your code here
def word_count(string):
    aantal = 1
    for item in string:
        if item == ' ':
            aantal +=1
    if len(string) ==0:
        aantal = 0
    return aantal