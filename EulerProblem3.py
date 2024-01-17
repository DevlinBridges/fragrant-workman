# Import the square root function from the math module
from math import sqrt 

# Define what the number for which we're looking for the largest prime factor
number = 600851475143

def main():
    prime_factors(number)

# Create prime_factors and run loop for numbers in range 3 to the square root of n
# Number is odd, so no even factors -> range starts at 3
# Largest factor cannot be greater than sqrt of the number
def is_prime(y):
    for n in range(3, int(sqrt(y))):
        if y % n == 0:
            return False
    return True

# Define prime_factors
# Create empty list to append values to
# Use same range and logic, but this time we append the relevant numbers to the list
def prime_factors(x): 
    my_list = []
    # Use loop to evaluate all numbers in range
    for z in range(3, int(sqrt(x))): 
        if x % z == 0: 
            # For each factor in range, z and x/z are also factors so we append them to our list
            if is_prime(z): 
                my_list.append(z) 
            if is_prime(x/z): 
                my_list.append(z) 
    # Use max to find largest int in list and print it for answer
    print(max(my_list)) 

main()
