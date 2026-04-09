n = 11  # 11x11 grid (0 to 10)
arena = [[1 for _ in range(n)] for _ in range(n)]  # 1 = safe, 0 = obstacle

# Each line in sample.txt: N E S W (distances from origin)
with open("sample.txt", "r") as f:
    for line in f:
        # Get the numbers from the line
        N, E, S, W = map(int, line.split())

        # Mark obstacles in the arena
        # North = up (decrease row)
        for i in range(1, N+1):
            row = 0 - i
            col = 0
            if 0 <= row < n:
                arena[row][col] = 0

        # East = right (increase column)
        for j in range(1, E+1):
            row = 0
            col = j
            if 0 <= col < n:
                arena[row][col] = 0

        # South = down (increase row)
        for i in range(1, S+1):
            row = i
            col = 0
            if 0 <= row < n:
                arena[row][col] = 0

        # West = left (decrease column)
        for j in range(1, W+1):
            row = 0
            col = 0 - j
            if 0 <= col < n:
                arena[row][col] = 0


print("Arena Map (1 = safe, 0 = obstacle):")
for row in arena:
    print(row)
