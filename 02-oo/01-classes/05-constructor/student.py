class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = depth * height * width
    '''  
    def volume(self):
        return self.depth*self.height*self.width
    '''