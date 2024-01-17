# We start the total at 0 and define x and y (first two numbers of the Fibonacci sequence) as 0 and 1.
# We impose the limit of y being less than 4 million.
# Using a while loop, we set x = y and y = x+y to generate the Fibonacci sequence.
# We only want even numbers, so we use an if statement in conjunction with the modulo function to assess if a number is even.
# Even numbers are added to the total and the total is printed.

total = 0
x, y = 0, 1
while y < 4000000:
    x, y = y, x + y
    if x % 2 == 0:
        continue
    total += x

print(total)
