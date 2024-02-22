# Write your code here

def process_data(string_data:list):
    dictionary = dict()
    for string in string_data:
        substring = string.split(',')
        dictionary[substring[0]] = {'age': int(substring[1]), 'courses': substring[2:]}
    return dictionary
def average_age(data:dict):
    amount = 0
    age = 0
    for minidict in data.values():
        age += int(minidict['age'])
        amount +=1
    return age/amount
def courses(data:dict):
    vakken = set()
    for minidict in data.values():
        for vak in minidict['courses']:
            vakken.add(vak)
    return vakken
def most_common_courses(data):
    vakken_aantal = {}
    for student in data.values():
        for vak in student['courses']:
            if vak not in vakken_aantal:
                vakken_aantal[vak] = 0
            vakken_aantal[vak] += 1
    vakken_list = []
    aantal_list = []
    index_te_verwijderen = []
    keeprunning = True
    for key in vakken_aantal.keys():
        vakken_list.append(key)
        aantal_list.append(vakken_aantal[key])
    while keeprunning:
    
        for i in range(len(vakken_list)):
            if aantal_list[i] < aantal_list[i-1]:
                index_te_verwijderen.append(i)
            
        for index in index_te_verwijderen:
            del vakken_list[index]
            del aantal_list [index]
        index_te_verwijderen = []

        if min(aantal_list) == max(aantal_list):
            keeprunning = False
    return set(vakken_list)
