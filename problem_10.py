# @author : Ibrahim Sma
# @github_location: https://github.com/ibrahim-sma
# @email: ibrahim.sma1990@gmail.com
# @LinkedIn: www.linkedin.com/in/ibrahim-sma


# Problem 10 -  Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


# Solution: Starts from if __name__ == "__main__":

# Note: This takes almost 5 seconds to complete, for faster results
# refer https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/

# importing function to check if a number is prime or not
from pyeuler import is_prime

# Function to calculate the sum of all prime numbers in the given range.
def sum_of_primes(num_range):
    
    # first prime number begins with 2; assigning the same.
    prime_sum = 2

    # We know all the even numbers expect 2 are not prime numbers.
    # Since 2 million is a huge range to loop, we have to skip even numbers in the range for faster results.

    for num in range(3, num_range, 2):
        if is_prime(num):
            prime_sum += num  
    return prime_sum

# Starts from here
if __name__ == "__main__":
    print("the sum of all the primes below two million is :", sum_of_primes(2000000))

