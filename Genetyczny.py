import random


# Funkcja celu
def objective_function(x):
    return x ** 2 + 4 * x + 4


# Klasa dla algorytmu genetycznego
class GeneticAlgorithm:
    def __init__(self, objective_function, lower_bound, upper_bound, population_size=30, generations=100,
                 mutation_rate=0.1, crossover_rate=0.9):
        self.objective_function = objective_function
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate

    def initialize_population(self):
        # Inicjalizacja populacji: losowe rozwiązania w zadanym zakresie
        self.population = [random.uniform(self.lower_bound, self.upper_bound) for _ in range(self.population_size)]

    def select_parents(self):
        # Selekcja rodziców: wybór dwóch najlepszych osobników
        sorted_population = sorted(self.population, key=self.objective_function)
        return sorted_population[0], sorted_population[1]

    def crossover(self, parent1, parent2):
        # Krzyżowanie: tworzymy potomstwo
        if random.random() < self.crossover_rate:
            # Punktowe krzyżowanie
            return (parent1 + parent2) / 2
        else:
            # Jeśli nie zachodzi krzyżowanie, zwracamy jeden z rodziców
            return parent1

    def mutate(self, offspring):
        # Mutacja: wprowadzenie losowej zmiany
        if random.random() < self.mutation_rate:
            return offspring + random.uniform(-1, 1)
        else:
            return offspring

    def evolve(self):
        # Główna pętla algorytmu genetycznego
        self.initialize_population()

        best_solution = min(self.population, key=self.objective_function)
        best_value = self.objective_function(best_solution)

        for generation in range(self.generations):
            new_population = []

            while len(new_population) < self.population_size:
                # Selekcja rodziców
                parent1, parent2 = self.select_parents()

                # Krzyżowanie
                offspring = self.crossover(parent1, parent2)

                # Mutacja
                offspring = self.mutate(offspring)

                # Dodanie potomstwa do nowej populacji
                new_population.append(offspring)

            # Uaktualnianie populacji
            self.population = new_population

            # Sprawdzanie najlepszego rozwiązania w danej generacji
            current_best_solution = min(self.population, key=self.objective_function)
            current_best_value = self.objective_function(current_best_solution)

            if current_best_value < best_value:
                best_solution = current_best_solution
                best_value = current_best_value

        return best_solution, best_value


if __name__ == "__main__":
    lower_bound = -10  # Dolny zakres
    upper_bound = 10  # Górny zakres

    ga = GeneticAlgorithm(objective_function, lower_bound, upper_bound)
    result, obj_value = ga.evolve()

    print("Znaleziony punkt minimum: {:.16f}".format(result))
    print("Wartość funkcji celu: {:.16f}".format(obj_value))
