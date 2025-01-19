def golden_section_search(objective_function, grad, x, lower_bound, upper_bound, tolerance=1e-6):
    phi = (1 + 5**0.5) / 2
    resphi = 2 - phi

    a, b = lower_bound, upper_bound
    c = a + resphi * (b - a)
    d = b - resphi * (b - a)

    while abs(c - d) > tolerance:
        if objective_function(x - c * grad) < objective_function(x - d * grad):
            b = d
        else:
            a = c

        c = a + resphi * (b - a)
        d = b - resphi * (b - a)

    return (b + a) / 2

def steepest_descent_with_golden_section(objective_function, x0, lower_bound=0, upper_bound=1, tolerance=1e-12, max_iterations=1000):
    x = x0
    iteration = 0

    while iteration < max_iterations:
        grad = 2 * x + 4  # Pochodna funkcji celu: f'(x) = 2x + 4

        if abs(grad) < tolerance:
            break

        step_size = golden_section_search(objective_function, grad, x, lower_bound, upper_bound)
        x_next = x - step_size * grad

        if abs(x_next - x) < tolerance:
            break

        x = x_next
        iteration += 1

    return x, objective_function(x)

if __name__ == "__main__":
    def objective_function(x):
        return x**2 + 4 * x + 4

    x0 = 0.0

    result, obj_value = steepest_descent_with_golden_section(objective_function, x0)

    print("Znaleziony punkt: {:.16f}".format(result))
    print("Wartość funkcji celu: {:.16f}".format(obj_value))
