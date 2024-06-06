class Cycle:
    def __init__(self, l) -> None:
        self.__l = list(l)
        self.__index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
            self.__index = (self.__index +1) % len(self.__l)
            return self.__l[self.__index]