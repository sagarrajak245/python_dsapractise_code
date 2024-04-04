def fractional_knapsack(weights, values, capacity):
    # Calculate value-to-weight ratios
    ratios = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
    # Sort items based on value-to-weight ratio in descending order
    ratios.sort(reverse=True)

    max_value = 0  # Initialize maximum value of items taken
    remaining_capacity = capacity  # Initialize remaining capacity of knapsack

    # Iterate through items
    for ratio, weight, value in ratios:
        # If weight of current item is less than or equal to remaining capacity,
        # take the whole item
        if weight <= remaining_capacity:
            max_value += value
            remaining_capacity -= weight
        # Otherwise, take a fraction of the item to fill the knapsack
        else:
            max_value += ratio * remaining_capacity
            break  # Knapsack is full, so stop iterating

    return max_value


# Example usage:
weights = [10, 20, 30]  # Weights of items
values = [60, 100, 120]  # Values of items
capacity = 50  # Capacity of knapsack

max_value = fractional_knapsack(weights, values, capacity)
print("Maximum value that can be obtained:", max_value)
