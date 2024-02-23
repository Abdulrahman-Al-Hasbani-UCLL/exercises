class Queue:
    def __init__(self):
        self.__lijst = []

    def add(self, item):
        self.__lijst.append(item)

    def next(self):
        item = self.__lijst[0]
        del self.__lijst[0]
        return item
    
    def is_empty(self):
        return len(self.__lijst) == 0