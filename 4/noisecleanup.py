import statistics

# Opening the file log.txt
with open("log.txt", "r") as f:
    data = f.read()

# Storing the log.txt file as a big list of values
values = list(map(float, data.split()))

# Implementing the sanchiko
def sanchiko(values, window_size):
    filtered = []
    # Loops through all the windows in the values list
    for i in range(len(values)-window_size+1):
        # Sets the individual window
        window = values[i: i + window_size]
        # Appends only the median of the window to the list
        filtered.append(statistics.median(window))

    return filtered

#Implementing muchiko
def muchiko(values, window_size):
    filtered = []
    # same as sanchiko but we find mean in place of median
    for i in range(len(values)-window_size+1):
        window = values[i: i + window_size]
        filtered.append(statistics.mean(window))
    return filtered

x = int(input("Enter the window size: "))

s_values = sanchiko(values, x)
m_values = muchiko(s_values, x-2)

print(m_values)
