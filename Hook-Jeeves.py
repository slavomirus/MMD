def hooke_jeeves(objective_function, x0, step_size=1.0, step_size_min=1e-6, alpha=0.5, max_iterations=1000):
    x_base = x0[:]
    x_best = x_base[:]
    iteration = 0

    while step_size > step_size_min and iteration < max_iterations:
        x_new = exploratory_search(objective_function, x_best, step_size)

        if objective_function(x_new) < objective_function(x_best):
            x_best = [2 * xn - xb for xn, xb in zip(x_new, x_base)]
            x_base = x_new[:]
        else:
            step_size *= alpha

        iteration += 1

    return x_best, objective_function(x_best)


def exploratory_search(objective_function, x, step_size):
    x_new = x[:]
    for i in range(len(x)):
        x_trial = x_new[:]
        x_trial[i] += step_size
        if objective_function(x_trial) < objective_function(x_new):
            x_new = x_trial[:]
        else:
            x_trial[i] -= 2 * step_size
            if objective_function(x_trial) < objective_function(x_new):
                x_new = x_trial[:]
    return x_new


if __name__ == "__main__":
    def objective_function(x):
        return x[0] ** 2 + 4 * x[0] + 4


    x0 = [0.0]

    result, obj_value = hooke_jeeves(objective_function, x0)

    print("Znaleziony punkt: {:.6f}".format(result))
    print("Wartość funkcji celu: {:.16f}".format(obj_value))
