from itertools import permutations

def find_shortest_path(distance, city_count):
    permutations_total = permutations(range(1,city_count)) #city 0 is the start and end

    shortest_tour = None
    shortest_distance = float('inf')
    for tour in permutations_total:
        tour = [0] + list(tour) + [0]

        tour_distance = sum(distance(tour[i], tour[i+1]) for i in range(city_count))
        
        if tour_distance < shortest_distance:
            shortest_distance = tour_distance
            shortest_tour = tour
    
    return shortest_tour