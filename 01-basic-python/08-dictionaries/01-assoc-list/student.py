#opnieuw doen

class AssocList:
    def __init__(self):
        self.items = []
    def __setitem__(self, key, value):
        index = self.__find_key_index(key)
        if index == -1:
            self.items.append([key, value])
        else:
            self.items[index][1] = value

    def __contains__(self, key):
        return self.__find_key_index(key) != -1

    def __getitem__(self, key):
        index = self.__find_key_index(key)
        if index == -1:
            raise KeyError()
        else:
            return self.items[index][1]

    def __len__(self):
        return len(self.items)

    def __find_key_index(self, key):
        for i in range(len(self.items)):
            k, v = self.items[i]
            if k == key:
                return i
        return -1
    
    def values(self):
        return [v for _, v in self.items]
    
    def keys(self):
        return [k for k, _ in self.items]