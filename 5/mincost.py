def minimum_wear_cost(limits, wear_factors, targets, D):
    l1, l2, l3 = limits
    w1, w2, w3 = wear_factors

    # To generate all the valid configurations for a given target
    def get_valid_configs(target):
        configs = []
        for inner in range(l1 + 1):
            for middle in range(l2 + 1):
                outer = target - inner - middle

                # Checking if the outer is still within limits
                if 0 <= outer <= l3:
                    # Checking the inner and outer stability condition
                    if abs(inner - outer) <= D:
                        configs.append((inner, middle, outer))

        return configs

    # Finding configs for all the targets
    all_configs = []
    for target in targets:
        all_configs.append(get_valid_configs(target))

    # Calculates the cost of movement for a given previous and current position
    def movement_cost(prev, curr):
        return (
            abs(prev[0] - curr[0]) * w1 +
            abs(prev[1] - curr[1]) * w2 +
            abs(prev[2] - curr[2]) * w3
        )

    min_total_cost = float('inf')

    # Brute force to find check all possible conditions
    def try_all_paths(target_index, previous_config, current_cost):
        nonlocal min_total_cost

        # Base case: all targets processed
        if target_index == len(targets):
            min_total_cost = min(min_total_cost, current_cost)
            return

        # Try every valid config for this particular target
        for config in all_configs[target_index]:
            cost = movement_cost(previous_config, config)
            try_all_paths(
                target_index + 1,
                config,
                current_cost + cost
            )

    # To start from initial position (0,0,0)
    try_all_paths(0, (0, 0, 0), 0)

    return min_total_cost
