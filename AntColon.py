import random
import math


class AntColony:
    def __init__(self, graph, n_ants, n_iterations, decay, alpha=1, beta=1):
        self.graph = graph  # Macierz odległości
        self.n_ants = n_ants  # Liczba mrówek
        self.n_iterations = n_iterations  # Liczba iteracji
        self.decay = decay  # Zanikanie feromonu
        self.alpha = alpha  # Wpływ feromonu
        self.beta = beta  # Wpływ odległości
        self.pheromone = [[1.0 for _ in range(len(graph))] for _ in range(len(graph))]  # Feromony początkowe

    def run(self):
        shortest_path = None
        shortest_distance = float('inf')

        for _ in range(self.n_iterations):
            all_paths = self.gen_all_paths()
            self.spread_pheronome(all_paths)

            for path, distance in all_paths:
                if distance < shortest_distance:
                    shortest_distance = distance
                    shortest_path = path

        return shortest_path, shortest_distance

    def spread_pheronome(self, all_paths):
        # Zmniejszamy feromony
        self.pheromone = [[pheromone * self.decay for pheromone in row] for row in self.pheromone]

        for path, distance in all_paths:
            # Zwiększamy feromon na ścieżkach odwiedzonych przez mrówki
            for i in range(len(path) - 1):
                self.pheromone[path[i]][path[i + 1]] += 1 / distance
                self.pheromone[path[i + 1]][path[i]] += 1 / distance

    def gen_all_paths(self):
        all_paths = []
        for _ in range(self.n_ants):
            path = self.gen_path(0)  # Zakładając, że mrówki zaczynają w wierzchołku 0
            distance = self.path_distance(path)
            all_paths.append((path, distance))
        return all_paths

    def gen_path(self, start):
        path = [start]
        visited = set(path)

        while len(path) < len(self.graph):
            current_node = path[-1]
            next_node = self.pick_next_node(current_node, visited)
            path.append(next_node)
            visited.add(next_node)

        return path

    def pick_next_node(self, current_node, visited):
        pheromone = []
        heuristic = []

        for i in range(len(self.graph)):
            if i not in visited:
                pheromone.append(self.pheromone[current_node][i] ** self.alpha)
                heuristic.append((1 / self.graph[current_node][i]) ** self.beta)
            else:
                pheromone.append(0)
                heuristic.append(0)

        pheromone = [p * h for p, h in zip(pheromone, heuristic)]
        total_pheromone = sum(pheromone)

        if total_pheromone == 0:
            prob = [1 / len(self.graph) for _ in range(len(self.graph))]
        else:
            prob = [p / total_pheromone for p in pheromone]

        return random.choices(range(len(self.graph)), prob)[0]

    def path_distance(self, path):
        return sum(self.graph[path[i]][path[i + 1]] for i in range(len(path) - 1))


# Przykładowy graf - odległości między wierzchołkami dla przestrzeni dyskretnej trzebaa jeszcze zrobić
graph = [
    [0, 1, 2, 5, 7],
    [1, 0, 2, 8, 2],
    [2, 2, 0, 1, 3],
    [5, 8, 1, 0, 1],
    [7, 2, 3, 1, 0]
]

# Parametry algorytmu
n_ants = 10  # Liczba mrówek
n_iterations = 100  # Liczba iteracji
decay = 0.95  # Zanikanie feromonu
alpha = 4  # Wpływ feromonu
beta = 4  # Wpływ odległości

# Tworzymy obiekt klasy AntColony i uruchamiamy algorytm
ant_colony = AntColony(graph, n_ants, n_iterations, decay, alpha, beta)
shortest_path, shortest_distance = ant_colony.run()

# Wyświetlamy wynik
print("Najkrótsza ścieżka: {:.16f}".format(shortest_path))
print("Najkrótsza odległość: {:.16f}".format(shortest_distance))