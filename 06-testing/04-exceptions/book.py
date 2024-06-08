class Book:
    def __init__(self, title, isbn) -> None:
        self.title = title
        self.isbn = isbn

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value:str):
        if not isinstance(value, str):
            raise RuntimeError
        if not value:
            raise RuntimeError
        if value.strip() == '':
            raise RuntimeError
        self.__title = value
    
    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, value):
        value = str(value)
        if value == '':
            raise RuntimeError
        '''
        if ' ' not in value or '-' not in value:
            raise RuntimeError
        '''
        nums = []
        for el in value:
            if el.isdigit():
                nums.append(int(el))
        
        if len(nums) != 13:
            raise RuntimeError
        
        calculated_nums = []
        for i in range(len(nums)):
            if i%2 == 0:
                calculated_nums.append(nums[i])
            else:
                calculated_nums.append(nums[i]*3)
        if sum(calculated_nums) %10 != 0:
            raise RuntimeError

        self.__isbn = value
