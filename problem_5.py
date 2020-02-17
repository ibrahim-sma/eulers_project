# @author : Ibrahim Sma
# @github_location: https://github.com/ibrahim-sma
# @email: ibrahim.sma1990@gmail.com
# @LinkedIn: www.linkedin.com/in/ibrahim-sma


# Problem 5 -  Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# Solution: Starts from if __name__ == "__main__":

# importing function to check if a number is prime or not
from problem_3 import is_prime

def smallest_multiple(number):

    multiple = 1
    for num in range(2, number + 1):

        # If the number is prime, multiplying it to the multiple
        if is_prime(num):
            multiple *= num

        else:
            # If the number is not prime and doesn't divide the product of multiple enters condition
            if not(multiple % num == 0):

                # Loop to identify the smallest factor of num
                for factor in range(2, num // 2 + 1):
                    if num % factor == 0:
                        break
                
                # Loop and multiply the smallest factor until product is divisible by num
                while True:
                    multiple *= factor
                    if multiple % num == 0:
                        break
    return multiple

# Starts from here
if __name__ == "__main__":
    print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is :", smallest_multiple(20))


# Solution Logic explanation:

# The smallest multiple which is evenly divisible from 1 to 6 is as follows:

# First multiply 1 * 2 * 3 * 4 * 5 * 6 = 720 (But this is largest multiple of the range)

# In this range let's breakdown the multiples into prime numbers and composite numbers

# product = 1 assigned initially and multiply the prime numbers.

# Prime nos are 2, 3, 5 and so the product is product - 1 * 2 * 3 * 5 = 30

# Composite nos are 4, 6; now check if 30 these is divisible of these numbers.

# 6 is divisible on 30; 30/6 = 5, hence we don't need to muliply 6 into the product.

# 4 is not divisible on 30; Now we don't need to multiply with 4 instead we have to identify the smallest factor of 4.

# Factors of 4 are 1, 2, 4; smallest factors is 2 excluding 1.

# Now keeping on multiplying the product with 2 so that it is divisible by 4. which is required only one time in case of 4.

# So the final product is product = 30 * 2 = 60. Hence 60 is the smallest multiple that is divisible by 1, 2, 3, 4, 5 and 6.
