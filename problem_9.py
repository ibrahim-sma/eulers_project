# @author : Ibrahim Sma
# @github_location: https://github.com/ibrahim-sma
# @email: ibrahim.sma1990@gmail.com
# @LinkedIn: www.linkedin.com/in/ibrahim-sma


# Problem 9 -  Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2 ; For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.


# Solution:

def pythagoras_product():
	
	# Initial assignment
	abc_prod = 0

	# Sum of given a,b,c in the question is 1000. 
	abc_sum = 1000

	# value of a,b,c has to be less than 1000; so that sum(a,b,c) will be 1000
	# Hence looping through a range less than 1000 for a & b

	for a in range(2,1000):
		for b in range(3, 1000):

			#  Since we have a & b from loop c can be found by subtracting (a & b) with 1000
			c = abc_sum - a - b
			
			# condition to check if a,b,c is a pythagoras triplet; returns the product if it is a triplet
			if (a**2 + b**2) == c**2:
				abc_prod = a * b * c
				return a, b, c, abc_prod

if __name__ == "__main__":
	a, b, c, abc_prod = pythagoras_product()
	print(f"The product of pythagoras triplet ({a},{b},{c}) whose sum is 1000 is, {abc_prod}")
