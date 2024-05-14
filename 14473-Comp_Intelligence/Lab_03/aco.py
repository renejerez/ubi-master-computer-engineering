import numpy as np
import random

class ACO:

    def __init__(self, num_cities, num_ants, num_iterations, decay, alpha, beta, coordinates=None):
        self.num_cities = num_cities
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        if coordinates is None:
            self.coordinates = [(0, 0)] * num_cities  # Default to origin if not specified
        else:
            self.coordinates = coordinates
        self.distances = np.full((num_cities, num_cities), np.inf)  # Initialize distances as infinite
        self.pheromone = np.ones((num_cities, num_cities)) * 1e-4
        self.ants = [{'current_city': None, 'visited': []} for _ in range(num_ants)]



    def ligaCidades(self):
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                if i != j:
                    self.distances[i][j] = self.distances[j][i] = self.euclidean_distance(self.coordinates[i], self.coordinates[j])

    def euclidean_distance(self, city1, city2):
        return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

    def probability(self, i, j, k):
        if j in self.ants[k]['visited']:
            return 0
        pheromone = self.pheromone[i][j] ** self.alpha
        heuristic = (1.0 / (self.distances[i][j] + 1e-10)) ** self.beta
        return pheromone * heuristic

    def calculate_route_length(self, route):
        return sum(self.distances[route[i]][route[i+1]] for i in range(len(route) - 1))

    def was_visited(self, city, ant):
        return 1 if city in self.ants[ant]['visited'] else 0

    def edge_in_route(self, i, j, ant):
        route = self.ants[ant]['visited']
        # Check if there's a direct edge from city i to city j in the route
        try:
            index_i = route.index(i)
            return 1 if route[(index_i + 1) % len(route)] == j else 0
        except ValueError:
            # If i is not in the route, it throws ValueError
            return 0


    def select_next_city(self, probabilities, current_route):
        total = sum(probabilities)
        if total == 0:  # Handling the case when all probabilities are zero
            unvisited_cities = [city for city in range(self.num_cities) if city not in current_route]
            return random.choice(unvisited_cities) if unvisited_cities else None
        normalized_prob = [p / total for p in probabilities]
        return random.choices(range(self.num_cities), weights=normalized_prob, k=1)[0]

    def construct_route(self, ant):
        current_city = random.randint(0, self.num_cities - 1)
        route = [current_city]
        ant['visited'] = [current_city]  # Initialize with the first city

        while len(route) < self.num_cities:
            probabilities = [self.probability(route[-1], j, self.ants.index(ant)) for j in range(self.num_cities)]
            next_city = self.select_next_city(probabilities, route)
            if next_city not in route:  # Make sure not to revisit cities within the same tour
                route.append(next_city)
                ant['visited'].append(next_city)  # Update visited list

        route.append(route[0])  # Complete the cycle by returning to the start
        ant['visited'] = route  # Assign full route


    def is_route_valid(self, route):
        return len(set(route[:-1])) == self.num_cities  # Ignore the return to start

    def update_pheromones(self):
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                if i != j:
                    self.pheromone[i][j] *= (1 - self.decay)  # Pheromone evaporation
                    for ant in self.ants:
                        if self.edge_in_route(i, j, self.ants.index(ant)):
                            self.pheromone[i][j] += 1.0 / self.calculate_route_length(ant['visited'])  # Pheromone deposit

    def optimize(self):
        best_route = None
        best_length = float('inf')
        for _ in range(self.num_iterations):
            for ant in self.ants:
                self.construct_route(ant)
                if self.is_route_valid(ant['visited']):
                    length = self.calculate_route_length(ant['visited'])
                    if length < best_length:
                        best_route, best_length = ant['visited'], length
            self.update_pheromones()
        return best_route, best_length

    def mostraRota(self, route):
        return ' -> '.join(map(str, route))

    
    def set_cities_connection(self, i, j):
        if i < self.num_cities and j < self.num_cities:
            self.distances[i][j] = self.euclidean_distance(self.coordinates[i], self.coordinates[j])
            self.distances[j][i] = self.distances[i][j]  # Ensure symmetry for an undirected graph

    def set_city_position(self, city, x, y):
        if city < self.num_cities:
            self.coordinates[city] = (x, y)
            for j in range(self.num_cities):
                if j != city:
                    self.set_cities_connection(city, j)  # Update distances for changed position

