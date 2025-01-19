import random

def monte_carlo_minimize(func, bounds, num_samples=10000):
    min_value = float('inf')
    min_point = None

    for _ in range(num_samples):
        sample = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(len(bounds))]
        value = func(sample)

        if value < min_value:
            min_value = value
            min_point = sample

    return min_point, min_value

if __name__ == "__main__":
    def sample_function(x):
        return x[0] ** 2 + 4 * x[0] + 4

    bounds = [(0, 3), (0, 3)]
    min_point, min_value = monte_carlo_minimize(sample_function, bounds)
    print("Minimum point:", min_point)
    print("Minimum value:", min_value)