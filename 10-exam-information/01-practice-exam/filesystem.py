# Enter your code here:
from abc import ABC, abstractmethod
class StorageDevice:
    def __init__(self, block_count:int, block_size:int) -> None:
        self.block_count = block_count
        self.__block_size = block_size
        self.__available_blocks = {x for x in range(0,block_count)}
        self.__used_blocks = set()
    
    @property
    def available_block_count(self):
        total = 0
        for x in self.__available_blocks:
            total+=1
        return total
    
    @property
    def used_block_count(self):
        total = 0
        for x in self.__used_blocks:
            total+=1
        return total
    
    @property
    def total_block_count(self):
        return self.block_count
    
    @property
    def block_size(self):
        return self.__block_size
    
    def allocate(self, block_count:int) -> list:
        if block_count > len(self.__available_blocks):
            raise RuntimeError
        
        reserved = list()
        for _ in range(block_count):
            block = self.__available_blocks.pop()
            reserved.append(block)
            self.__used_blocks.add(block)

        return reserved
    
    def free(self, blocks:list) -> None:
        for i in blocks:
            if i not in self.__used_blocks:
                raise RuntimeError
            
        for block in blocks:
            self.__used_blocks.remove(block)
            self.__available_blocks.add(block)

    
class Entity(ABC):
    def __init__(self, storage:StorageDevice,name:str, ) -> None:
        self.__storage = storage
        if not self.is_valid_name(name):
            raise RuntimeError
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name:str):
        if self.is_valid_name(new_name) == True:
            self.__name = new_name
        else:
            raise RuntimeError
    
    @staticmethod
    def is_valid_name(name:str) ->bool:
        if len(name) > 16:
            return False
        if len(name) <1:
            return False

        return all(char.isalnum() or char == '.' for char in name)
    
    @property
    def storage(self):
        return self.__storage
    
    @property
    @abstractmethod
    def size_in_blocks(self):
        ...
    
    @property
    def size_in_bytes(self):
        return self.size_in_blocks*self.__storage.block_size
    
    @abstractmethod
    def clear(self):
        ...

class File(Entity):
    def __init__(self, storage: StorageDevice, name: str) -> None:
        super().__init__(storage, name)
        self.__used_blocks = []
    
    def grow(self, block_count:int) -> None:
        templ = self.storage.allocate(block_count)
        self.__used_blocks.extend(x for x in templ if x not in self.__used_blocks)

    def clear(self):
        self.storage.free(self.__used_blocks)
        self.__used_blocks.clear()
    
    @property
    def size_in_blocks(self):
        return len(self.__used_blocks)

class Directory(Entity):
    def __init__(self, storage: StorageDevice, name: str) -> None:
        super().__init__(storage, name)
        self.__children = list()

    @property
    def size_in_blocks(self) -> int:
        total = 0
        for item in self.__children:
            total += item.size_in_blocks
        return total
    
    def add(self, entity: Entity) -> None:
        self.__children.append(entity)

    def clear(self):
        for item in self.__children:
            item.clear()
        self.__children.clear()

