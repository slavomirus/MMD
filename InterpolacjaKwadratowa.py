def quadratic_interpolation(objective_function, lower_bound, upper_bound, tolerance=1e-6, max_iterations=100):
    # Początkowe trzy punkty
    x0 = lower_bound
    x2 = upper_bound
    x1 = (x0 + x2) / 2

    f0 = objective_function(x0)
    f1 = objective_function(x1)
    f2 = objective_function(x2)

    iteration = 0

    while iteration < max_iterations:
        # Wyznaczanie współczynników a, b, c dla funkcji kwadratowej przez interpolację trzech punktów
        denom = (x0 - x1) * (x0 - x2) * (x1 - x2)

        a = (x1 * (f0 - f2) + x2 * (f1 - f0) + x0 * (f2 - f1)) / denom
        b = ((x1 ** 2) * (f0 - f2) + (x2 ** 2) * (f1 - f0) + (x0 ** 2) * (f2 - f1)) / denom
        c = ((x1 ** 3) * (f0 - f2) + (x2 ** 3) * (f1 - f0) + (x0 ** 3) * (f2 - f1)) / denom

        # Miejsce zerowe pochodnej funkcji kwadratowej
        vertex = -b / (2 * a)  # Wyznaczenie punktu minimum

        # Obliczanie wartości funkcji w punkcie vertex
        f_vertex = objective_function(vertex)

        # Sprawdzanie kryterium zatrzymania
        if abs(vertex - x1) < tolerance:
            break

        # Przesuwanie punktów
        x0, x1, x2 = x1, vertex, x2
        f0, f1, f2 = f1, f_vertex, f2

        iteration += 1

    return vertex, f_vertex


if __name__ == "__main__":
    def objective_function(x):
        return x ** 2 + 4 * x + 4


    lower_bound = -10
    upper_bound = 10

    result, obj_value = quadratic_interpolation(objective_function, lower_bound, upper_bound)

    print("Znaleziony punkt: {:.16f}".format(result))
    print("Wartość funkcji celu: {:.16f}".format(obj_value))
