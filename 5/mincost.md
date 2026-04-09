1. Generate all valid configurations (inner, middle, outer) such that:
    inner + middle + outer = target
    0 ≤ inner ≤ l1, 0 ≤ middle ≤ l2, 0 ≤ outer ≤ l3
    |inner - outer| ≤ D
2. Try all possible configurations for each target (brute force recursion)
3. Calculate movement cost:
    cost = |Δinner| * w1 + |Δmiddle| * w2 + |Δouter| * w3
4. Start from: (0, 0, 0)
5. Keep track of the minimum total cost
6. Take the minimum cost route
