class Time:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self, value):
        if 0 <= value < 24:
            self.__hours = value
        else:
            raise ValueError()
        
    @property
    def minutes(self):
        return self.__minutes
    
    @minutes.setter
    def minutes(self, value):
        if 0 <= value < 60:
            self.__minutes = value
        else:
            raise ValueError()
        
    @property
    def seconds(self):
        return self.__seconds
    
    @seconds.setter
    def seconds(self, value):
        if 0 <= value < 60:
            self.__seconds = value
        else:
            raise ValueError()