import random


# Funkcja celu
def objective_function(x):
    return x ** 2 + 4 * x + 4


# Klasa Particle reprezentująca cząsteczkę w przestrzeni
class Particle:
    def __init__(self, lower_bound, upper_bound):
        self.position = random.uniform(lower_bound, upper_bound)
        self.velocity = random.uniform(-1, 1)
        self.best_position = self.position
        self.best_value = objective_function(self.position)

    def move(self, w, c1, c2, r1, r2, gbest_position):
        # Aktualizacja prędkości
        self.velocity = w * self.velocity + c1 * r1 * (self.best_position - self.position) + c2 * r2 * (
                    gbest_position - self.position)

        # Aktualizacja pozycji
        self.position += self.velocity

        # Obliczanie nowej wartości funkcji
        value = objective_function(self.position)

        # Aktualizacja najlepszej pozycji cząsteczki
        if value < self.best_value:
            self.best_position = self.position
            self.best_value = value


# Funkcja PSO
def pso(objective_function, lower_bound, upper_bound, num_particles=30, max_iterations=100, tolerance=1e-6):
    # Parametry PSO
    w = 0.5  # Współczynnik inercji
    c1 = 1.5  # Współczynnik przyciągania do pbest
    c2 = 1.5  # Współczynnik przyciągania do gbest

    # Inicjalizacja cząsteczek
    particles = [Particle(lower_bound, upper_bound) for _ in range(num_particles)]

    # Inicjalizacja najlepszej pozycji grupy (gbest)
    gbest_position = min(particles, key=lambda p: p.best_value).best_position
    gbest_value = objective_function(gbest_position)

    # Główna pętla algorytmu
    iteration = 0
    while iteration < max_iterations:
        for particle in particles:
            # Ruch cząsteczek
            r1 = random.random()
            r2 = random.random()
            particle.move(w, c1, c2, r1, r2, gbest_position)

            # Aktualizacja gbest
            if particle.best_value < gbest_value:
                gbest_position = particle.best_position
                gbest_value = particle.best_value

        # Sprawdzanie kryterium zatrzymania
        if abs(gbest_value) < tolerance:
            break

        iteration += 1

    return gbest_position, gbest_value


if __name__ == "__main__":
    lower_bound = -10  # Dolny zakres
    upper_bound = 10  # Górny zakres

    result, obj_value = pso(objective_function, lower_bound, upper_bound)

    print("Znaleziony punkt minimum: {:.16f}".format(result))
    print("Wartość funkcji celu: {:.16f}".format(obj_value))
