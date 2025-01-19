import random

def monte_carlo_minimization(objective_function, lower_bound, upper_bound, iterations=10000):
    best_x = None
    best_f = float('inf')

    for _ in range(iterations):
        x = random.uniform(lower_bound, upper_bound)
        f = objective_function(x)

        if f < best_f:
            best_x = x
            best_f = f

    return best_x, best_f

if __name__ == "__main__":
    def objective_function(x):
        return x**2 + 4 * x + 4

    lower_bound = -10
    upper_bound = 10

    result, obj_value = monte_carlo_minimization(objective_function, lower_bound, upper_bound)

    print("Znaleziony punkt: {:.6f}".format(result))
    print("Wartość funkcji celu: {:.16f}".format(obj_value))
