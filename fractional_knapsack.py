# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    value_per_kg = [j/weights[i] for i,j in enumerate(values)]
    weight_values = dict(zip(value_per_kg, weights ))
    value_per_kg = sorted(value_per_kg, key=float, reverse=True)
    for item in value_per_kg:
        if capacity <= 0:
            break
        elif capacity < weight_values[item]:
            value = value + ((capacity/weight_values[item]) * (weight_values[item]*item))
            break
        capacity = capacity - weight_values[item]
        value = value + (item * weight_values[item])
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
