import random


# Funkcja celu
def objective_function(x):
    return x ** 2 + 4 * x + 4


# Algorytm różnicowy (Differential Evolution)
def differential_evolution(objective_function, lower_bound, upper_bound, num_individuals=30, max_iterations=100,
                           tolerance=1e-6):
    # Parametry algorytmu
    F = 0.8  # Współczynnik mutacji
    CR = 0.9  # Współczynnik krzyżowania

    # Inicjalizacja populacji
    population = [random.uniform(lower_bound, upper_bound) for _ in range(num_individuals)]

    # Inicjalizacja najlepszego rozwiązania
    best_solution = min(population, key=objective_function)
    best_value = objective_function(best_solution)

    # Główna pętla algorytmu
    iteration = 0
    while iteration < max_iterations:
        for i in range(num_individuals):
            # Selekcja trzech różnych osobników
            a, b, c = random.sample([x for x in population if x != population[i]], 3)

            # Mutacja
            mutant = a + F * (b - c)

            # Krzyżowanie
            crossover = [mutant if random.random() < CR else population[i] for j in range(1)]

            # Selekcja
            new_solution = crossover[0]
            new_value = objective_function(new_solution)
            if new_value < objective_function(population[i]):
                population[i] = new_solution

                # Aktualizacja najlepszego rozwiązania
                if new_value < best_value:
                    best_solution = new_solution
                    best_value = new_value

        # Sprawdzanie kryterium zatrzymania
        if abs(best_value) < tolerance:
            break

        iteration += 1

    return best_solution, best_value


if __name__ == "__main__":
    lower_bound = -10  # Dolny zakres
    upper_bound = 10  # Górny zakres

    result, obj_value = differential_evolution(objective_function, lower_bound, upper_bound)

    print("Znaleziony punkt minimum: {:.16f}".format(result))
    print("Wartość funkcji celu: {:.16f}".format(obj_value))
