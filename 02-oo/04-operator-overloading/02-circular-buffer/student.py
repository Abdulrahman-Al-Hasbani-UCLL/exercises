class CircularBuffer:

    def __init__(self, n):
        self.n = n
        self.__buffer = []
    @property
    def buffer(self):
        return self.__buffer
    def __getitem__(self, index):
        return self.__buffer[index]
    
    def add(self, element):
        if len(self.__buffer) < self.n:
            self.__buffer.append(element)
        else:
            del self.__buffer[0]
            self.__buffer.append(element)
    
    def __len__(self):
        return len(self.__buffer)
    