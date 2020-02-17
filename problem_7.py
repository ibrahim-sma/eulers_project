# @author : Ibrahim Sma
# @github_location: https://github.com/ibrahim-sma
# @email: ibrahim.sma1990@gmail.com
# @LinkedIn: www.linkedin.com/in/ibrahim-sma


# Problem 7 -  10001st prime

# The sum of the squares of the first ten natural numbers is, 12+22+...+102=385

# The square of the sum of the first ten natural numbers is, (1+2+...+10)2=552=3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.



# Solution: Starts from if __name__ == "__main__":

# importing function to check if a number is prime or not
# from problem_3 import is_prime

import math

def is_prime(num):
    if num == 2:
        return True
    elif num == 1:
        return False
    else:
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                break
        else:
            return True

        return False

def nth_prime(number):

    prime_count = 0
    num = 1
    product = 1

    while prime_count < number:

        if product % num == 0:
            num += 1
            continue
        else:
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
