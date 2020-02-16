# @author : Ibrahim Sma
# @github_location: https://github.com/ibrahim-sma
# @email: ibrahim.sma1990@gmail.com
# @LinkedIn: www.linkedin.com/in/ibrahim-sma


# Problem 3 -  Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def is_prime(num):
	for i in range(2, int(num / 2) + 1):
		if num % i == 0:
			break
	else:
		return True

	return False

current_prime_factor = 0  ## Temporary assignment

input_number = 600851475143
largest_prime_factor = input_number

while True:
	exit_for_loop = False

	for num in range(2, largest_prime_factor // 2 + 1):
		if exit_for_loop:
			break
		if largest_prime_factor % num == 0:
			if is_prime(num):
				if num > current_prime_factor:
					current_prime_factor = num
					largest_prime_factor = largest_prime_factor // current_prime_factor
					exit_for_loop = True
	else:
		break

print(f"The largest prime_factor of {input_number} is {largest_prime_factor}")

# ***** Solution guidelines *****

# Additional Description:

# Factors - for number 18 - 1, 2, 3, 6, 9, 18 are the factors

# Prime number - Any number that is divisible only by itself 
# is called prime number. i.e. A prime number has factor as the number 
# itself and 1. e.g 13 - factors of 13 are 1 and 13
# So 3 is the largest prime factor of 18


# Code Logic Understanding:
# i) First we have to findout the factors of number 600851475143
# ii) If a number is a factor it has to be a prime number as per question

# But since, 600851475143 is very huge number this will take lot of time looping
# hence we have to break down. Here is an example, prime factors of 210 are 2, 3, 5, 7
# Instead of looping till 210 we can break like this, 
# keep dividing the smallest prime number from 210.
# So first looping will be till 210/2 -> 105; then 105 / 3 -> 35 and so on so that loop count is reduced.

# The prime factors of 600851475143 are 71, 839, 1471, 6857