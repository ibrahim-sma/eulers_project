# @author : Ibrahim Sma
# @github_location: https://github.com/ibrahim-sma
# @email: ibrahim.sma1990@gmail.com
# @LinkedIn: www.linkedin.com/in/ibrahim-sma


# Problem 4 -  Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Solution: Start reading from if __name__ == "__main__":

def palindrome_function(numbers):

    # Assiging variables to capture the current largest palindrome and 
    # the corresponding 3 digit numbers
    number_1 = 0
    number_2 = 0
    palindrome = 0

    for num1 in numbers:
        for num2 in numbers:

            product = num1 * num2

            # Checking if the product obtained is a palindrome
            if str(product) == str(product)[::-1]:
                if product > palindrome:
                    palindrome = product
                    number_1 = num1
                    number_2 = num2

                # To avoid looping below the largest palindrome this is required
                if num1 < number_2:
                    return palindrome

# Start from here
if __name__ == "__main__":
    
    # Creating a list of 3 digit numbers starting with 999 and end with 100
    numbers = list(range(100,1000))[::-1]

    print(palindrome_function(numbers))
