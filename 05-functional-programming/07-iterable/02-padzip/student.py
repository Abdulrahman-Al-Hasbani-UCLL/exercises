class PadZip:
    def __init__(self, list1, list2, padding=None):
        self.__list1 = iter(list1)
        self.__list2 = iter(list2)
        self.__padding = padding
    
    def __iter__(self):
        return self
    
    def __next__(self):
        end_reached = 0

        try:
            list1 = next(self.__list1)
        except StopIteration:
            list1 = self.__padding
            end_reached += 1

        try:
            list2 = next(self.__list2)
        except StopIteration:
            list2 = self.__padding
            end_reached += 1

        if end_reached == 2:
            raise StopIteration()

        return (list1, list2)