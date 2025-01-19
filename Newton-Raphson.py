def newton_raphson(objective_function, derivative, second_derivative, initial_guess, tolerance=1e-6,
                   max_iterations=100):
    x_n = initial_guess
    iteration = 0

    while iteration < max_iterations:
        f_prime = derivative(x_n)
        f_double_prime = second_derivative(x_n)

        # Sprawdzanie, czy druga pochodna jest zerowa (unikamy dzielenia przez zero)
        if f_double_prime == 0:
            print("Druga pochodna wynosi zero, metoda Newtona-Raphsona nie jest odpowiednia.")
            return None

        # Nowa wartość x
        x_n1 = x_n - f_prime / f_double_prime

        # Sprawdzanie kryterium zatrzymania
        if abs(x_n1 - x_n) < tolerance:
            return x_n1

        x_n = x_n1
        iteration += 1

    print("Przekroczono maksymalną liczbę iteracji.")
    return x_n


if __name__ == "__main__":
    # Funkcja celu
    def objective_function(x):
        return x ** 2 + 4 * x + 4


    # Pierwsza pochodna
    def derivative(x):
        return 2 * x + 4


    # Druga pochodna
    def second_derivative(x):
        return 2


    initial_guess = -10  # Punkt początkowy

    result = newton_raphson(objective_function, derivative, second_derivative, initial_guess)

    if result is not None:
        print("Znaleziony punkt minimum: {:.16f}".format(result))
        print("Wartość funkcji celu: {:.16f}".format(objective_function(result)))
