def golden_section_search(objective_function, lower_bound, upper_bound, tolerance=1e-6):
    phi = (1 + 5**0.5) / 2  # Złota liczba
    resphi = 2 - phi

    a, b = lower_bound, upper_bound
    c = a + resphi * (b - a)
    d = b - resphi * (b - a)

    while abs(c - d) > tolerance:
        if objective_function(c) < objective_function(d):
            b = d
        else:
            a = c

        c = a + resphi * (b - a)
        d = b - resphi * (b - a)

    return (b + a) / 2

if __name__ == "__main__":
    def objective_function(x):
        return x**2 + 4 * x + 4

    lower_bound = -10
    upper_bound = 10

    result = golden_section_search(objective_function, lower_bound, upper_bound)

    print("Znaleziony punkt: {:.16f}".format(result))
    print("Wartość funkcji celu: {:.16f}".format(objective_function(result)))
