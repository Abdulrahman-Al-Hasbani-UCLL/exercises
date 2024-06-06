class Repeat:
    def __init__(self, amount):
        self.__amount = amount
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.__amount