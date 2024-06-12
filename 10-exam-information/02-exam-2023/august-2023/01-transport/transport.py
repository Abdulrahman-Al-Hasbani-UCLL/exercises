# enter your code here to solve the transporation assignment
# voer hier je code in om de vervoersvraag op te lossen
from abc import ABC, abstractmethod

class Passenger:
    @staticmethod
    def is_valid_name(name:str) -> bool:
        if ' ' not in name:
            return False
        if len(name.split()) <2:
            return False
        return True
    
    def __init__(self, id:str, name:str, money:int) -> None:
        self.id = id
        if not self.is_valid_name(name):
            raise ValueError
        self.__name = name
        self.money = money

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, n_name:str):
        if self.is_valid_name(n_name):
            self.__name = n_name
        else:
            raise ValueError
        
class Vehicle(ABC):

    def __init__(self, license_plate:str, amount_of_seats:int) -> None:
        self.license_plate= license_plate
        self.amount_of_seats = amount_of_seats
        self.__occupants = dict()
    
    @property
    def number_of_occupants(self):
        return len(self.__occupants.keys())
    
    @property
    @abstractmethod
    def maximum_occupants(self):
        ...
    
    def add_passenger(self, passenger: Passenger):
        self.__occupants[passenger.id] = passenger
    
    def remove_passenger(self, passenger: Passenger):
        del self.__occupants[passenger.id]
    
    def remove_all_passengers(self):
        self.__occupants.clear()
    
    @property
    def occupant_names(self):
        names = list()
        for key in self.__occupants.keys():
            names.append(self.__occupants[key].name)
        return names
    
class Taxi(Vehicle):
    def __init__(self, license_plate: str, amount_of_seats: int) -> None:
        super().__init__(license_plate, amount_of_seats)
        self.is_available = True
    
    @property
    def maximum_occupants(self):
        return self.amount_of_seats
    
    def pickup(self, passengers:list[Passenger], distance):
        if self.number_of_occupants == self.maximum_occupants or self.is_available == False or len(passengers)> self.maximum_occupants:
            raise ValueError
        
        first_passenger = None
        for _ in range(1):
            first_passenger = passengers[0]
        if first_passenger.money < (1+distance)+5:
            raise RuntimeError
        if 1+distance <5:
            first_passenger.money -= 5
        else:
            first_passenger.money -= (1+distance)
        passengers[0] = first_passenger

        self.is_available = False
        for item in passengers:
            self.add_passenger(item)
    
    def dropoff(self):
        self.remove_all_passengers()
        self.is_available = True

class Bus(Vehicle):
    def __init__(self, license_plate: str, amount_of_seats: int) -> None:
        super().__init__(license_plate, amount_of_seats)
    
    @property
    def maximum_occupants(self):
        return self.amount_of_seats*2
     
    def board(self, passenger:Passenger):
        if self.maximum_occupants == self.number_of_occupants or passenger.money < 2 :
            raise RuntimeError

        passenger.money -= 2
        self.add_passenger(passenger)
    
    def disembark(self, passenger:Passenger):
        self.remove_passenger(passenger)