import statistics

with open("log.txt", "r") as f:
    data = f.read()

values = list(map(float, data.split()))

def sanchiko(values, window_size):
    filtered = []

    for i in range(len(values)-window_size+1):
        window = values[i: i + window_size]
        filtered.append(statistics.median(window))

    return filtered

def muchiko(values, window_size):
    filtered = []
    for i in range(len(values)-window_size+1):
        window = values[i: i + window_size]
        filtered.append(statistics.mean(window))
    return filtered

x = int(input("Enter the window size: "))

s_values = sanchiko(values, x)
m_values = muchiko(s_values, x-2)

print(m_values)
