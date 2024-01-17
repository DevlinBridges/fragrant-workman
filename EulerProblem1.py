# Use range to produce all integers 0-999
# Use loop to iterate over all numbers divisible by 3 or 5
# Use sum to print n, which is all numbers divisible by 3 or 5
print(sum(n for n in range(1000) if n % 3 == 0 or n % 5 == 0))
