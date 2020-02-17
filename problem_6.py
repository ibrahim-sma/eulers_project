# @author : Ibrahim Sma
# @github_location: https://github.com/ibrahim-sma
# @email: ibrahim.sma1990@gmail.com
# @LinkedIn: www.linkedin.com/in/ibrahim-sma


# Problem 6 -  Sum square difference

# The sum of the squares of the first ten natural numbers is, 12+22+...+102=385

# The square of the sum of the first ten natural numbers is, (1+2+...+10)2=552=3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# Solution: Starts from if __name__ == "__main__":

def sum_square_difference(number):
    
    sum_of_squares = 0
    square_of_sums = 0

    while number > 0:
        sum_of_squares += number ** 2
        square_of_sums += number
        number -= 1

    # print(sum_of_squares)
    # print(square_of_sums ** 2)

    difference = square_of_sums ** 2 - sum_of_squares
    # print(difference)

    return difference


# Starts from here
if __name__ == "__main__":
    print("difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is :", sum_square_difference(100))


# Solution Logic explanation:

# Assign variables to capture sum_of_squares & square_of_sums

# Loop through upto the range (100) and add to square_of_sums and sum_of_squares

# Find the difference between square_of_sums and sum_of_squares

# return the differnce output