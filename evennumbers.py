import statistics

start, end = 1, 10000

# iterating each number in list
for num in range(start, end + 1):

    # checking condition
    if num % 2 == 0:
        print(num, end=" ")
    x = statistics.mean(range(start, end + 1))
            print(x)