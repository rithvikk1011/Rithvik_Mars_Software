This program reads numerical data from a file and applies two types of filtering:

Median filter (Sanchiko)
Mean filter (Muchiko)

These filters help smooth noisy data.

Input:
A file log.txt containing numbers
Window size x (entered by user)
1.Read Data:
File is opened and read as a string
Converted into a list of float values
values = list(map(float, data.split()))

2. Sanchiko:
Take a window of size window_size
Compute the median of each window
Store results in a new list
Formula: median = statistics.median(window)

3. Muchiko:
Similar to Sanchiko
Instead of median, compute the mean (average)
Formula: mean = statistics.mean(window)

4. Flow
Apply Sanchiko on original data
Apply Muchiko on the result of Sanchiko
