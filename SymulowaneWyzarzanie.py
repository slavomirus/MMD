import random
import math

def simulated_annealing(objective_function, x0, initial_temp=1000, cooling_rate=0.99, temp_min=1e-6, max_iterations=1000):
    x_current = x0
    f_current = objective_function(x_current)
    temp = initial_temp
    iteration = 0

    while temp > temp_min and iteration < max_iterations:
        x_new = x_current + random.uniform(-1, 1) * temp
        f_new = objective_function(x_new)

        if f_new < f_current or math.exp((f_current - f_new) / temp) > random.random():
            x_current = x_new
            f_current = f_new

        temp *= cooling_rate
        iteration += 1

    return x_current, f_current

if __name__ == "__main__":
    def objective_function(x):
        return x**2 + 4 * x + 4

    x0 = 0.0

    result, obj_value = simulated_annealing(objective_function, x0)

    print("Znaleziony punkt: {:.6f}".format(result))
    print("Wartość funkcji celu: {:.16f}".format(obj_value))
