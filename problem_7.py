# @author : Ibrahim Sma
# @github_location: https://github.com/ibrahim-sma
# @email: ibrahim.sma1990@gmail.com
# @LinkedIn: www.linkedin.com/in/ibrahim-sma


# Problem 7 -  10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


# Solution: Starts from if __name__ == "__main__":

# importing function to check if a number is prime or not
from pyeuler import is_prime

def nth_prime(number):

    prime_count = 0
    num = 1
    product = 1

    while prime_count < number:
        if not(is_prime(num)):
            num += 1
            continue
        else:
            product *= num

            num += 1
            prime_count += 1

    return num - 1

# Starts from here
if __name__ == "__main__":
    print("10001th prime number is :", nth_prime(10001))
