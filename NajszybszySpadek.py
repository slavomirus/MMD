def steepest_descent(objective_function, x0, step_size=0.1, tolerance=1e-12, max_iterations=1000):
    x = x0
    iteration = 0

    while iteration < max_iterations:
        grad = 2 * x + 4  # Pochodna funkcji celu: f'(x) = 2x + 4
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

    result, obj_value = steepest_descent(objective_function, x0)

    print("Znaleziony punkt: {:.16f}".format(result))
    print("Wartość funkcji celu: {:.16f}".format(obj_value))
