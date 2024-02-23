# Write your code here
class Time:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self,value):
        if value >23 or value <0:
            raise ValueError()
        self.__hours = value
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property 
    def seconds(self):
        return self.__seconds
    
    @minutes.setter
    def minutes(self, value):
        if value < 0 or value >59:
            raise ValueError()
        self.__minutes = value
    @seconds.setter
    def seconds(self, value):
        if value < 0 or value >59:
            raise ValueError()
        self.__seconds = value
    