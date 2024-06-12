# Write your own tests for the transport.py file here.
# You must include the tests asked for in the assignment for full credit.
# You may add additional tests if you would like to test your code more thoroughly.
# Additional tests will not result in a higher grade.
# This file must be able to be run without error in order to receive credit for the required testing.
####
# Schrijf hier je eigen tests voor het transport.py bestand.
# Je moet de gevraagde tests in de opdracht opnemen voor volledige waardering.
# Je mag extra tests toevoegen als je je code grondiger wilt testen.
# Extra tests zullen niet leiden tot een hoger cijfer.
# Dit bestand moet zonder fouten uitgevoerd kunnen worden om punten te krijgen voor de vereiste testen.

import pytest
from transport import *
@pytest.mark.parametrize(('nummerplaat','aantal_stoelen', 'lijst_passagiers', 'afstand'), [
    ("ABC123", 4, [Passenger("1", "Alice pain", 100), Passenger("2", "Bob b", 15)], 5),
    ("XYZ789", 2, [Passenger("3", "Charlie evens", 200), Passenger("4", "Dave d", 25)], 10),
    ("DEF456", 3, [Passenger("5", "Eve t", 300), Passenger("6", "Frank f", 35)], 15)
])
def test_valid_taxi_max_occupants_succeeds(nummerplaat, aantal_stoelen, lijst_passagiers, afstand):
    voorbeeld_taxi = Taxi(nummerplaat, aantal_stoelen)
    
    assert voorbeeld_taxi.is_available == True

    voorbeeld_taxi.pickup(lijst_passagiers, afstand)

    assert voorbeeld_taxi.amount_of_seats == aantal_stoelen
    assert voorbeeld_taxi.number_of_occupants == len(lijst_passagiers)
    assert voorbeeld_taxi.is_available == False
    assert voorbeeld_taxi.license_plate == nummerplaat
    #De belanrijke
    assert voorbeeld_taxi.maximum_occupants == aantal_stoelen, f'De Taxi.maximum_occupants functie moet het zelfde zijn als het aantal stoelen.\n {voorbeeld_taxi.maximum_occupants} is niet het juiste resultaat, \n het juiste resultaat is: {aantal_stoelen}'

@pytest.mark.parametrize(('nummerplaat','aantal_stoelen', 'lijst_passagiers', 'afstand'), [
    ("ABC123", 3, [Passenger("1", "Alice pain", 100), Passenger("2", "Bob b", 15), Passenger("5", "Eve t", 300), Passenger("6", "Frank f", 35)], 5),
    ("XYZ789", 1, [Passenger("3", "Charlie evens", 200), Passenger("4", "Dave d", 25)], 10),
    ("DEF456", 0, [Passenger("5", "Eve t", 300)], 15)
])
def test_valid_taxi_max_occupants_fails(nummerplaat, aantal_stoelen, lijst_passagiers, afstand):
    voorbeeld_taxi = Taxi(nummerplaat, aantal_stoelen)
    
    assert voorbeeld_taxi.is_available == True

    with pytest.raises(ValueError):
        voorbeeld_taxi.pickup(lijst_passagiers, afstand)


@pytest.mark.parametrize(('license_plate','number_of_seats', 'passenger_list'), [
    ("ABC123", 4, [Passenger("1", "Alice pain", 100), Passenger("2", "Bob b", 15)]),
    ("XYZ789", 2, [Passenger("3", "Charlie evens", 200), Passenger("4", "Dave d", 25)]),
    ("DEF456", 3, [Passenger("5", "Eve t", 300), Passenger("6", "Frank f", 35)])
])
def test_valid_bus_max_occupants_succeeds(license_plate, number_of_seats, passenger_list):
    example_bus = Bus(license_plate, number_of_seats)
    
    for passenger in passenger_list:
        example_bus.board(passenger)

    assert example_bus.amount_of_seats == number_of_seats
    assert example_bus.number_of_occupants == len(passenger_list)
    assert example_bus.license_plate == license_plate
    assert example_bus.maximum_occupants == number_of_seats * 2, f'The Bus.maximum_occupants function should be twice the number of seats.\n {example_bus.maximum_occupants} is not the correct result, \n the correct result is: {number_of_seats * 2}'

@pytest.mark.parametrize(('license_plate','number_of_seats', 'passenger_list'), [
    ("ABC123", 2, [Passenger("1", "Alice pain", 100), Passenger("2", "Bob b", 15), Passenger("5", "Eve t", 300), Passenger("6", "Frank f", 35), Passenger("9", "Eve t2", 300)]),
    ("XYZ789", 1, [Passenger("3", "Charlie evens", 200), Passenger("4", "Dave d", 25), Passenger("9", "Eve t2", 300)]),
    ("DEF456", 0, [Passenger("5", "Eve t", 300)])
])
def test_valid_bus_max_occupants_fails(license_plate, number_of_seats, passenger_list):
    example_bus = Bus(license_plate, number_of_seats)
    
    with pytest.raises(RuntimeError):
        for passenger in passenger_list:
            example_bus.board(passenger)