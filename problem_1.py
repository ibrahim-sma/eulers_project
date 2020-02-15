## Problem 1 -  Multiples of 3 and 5

##If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
##
##Find the sum of all the multiples of 3 or 5 below 1000.


total = 0
for number in range(1, 1000):
    if number % 3 == 0 or number % 5 == 0:
        total += number
print(f'The sum of all the multiples of 3 or 5 below 1000 is : {total}')


## Solution guidelines:

##1) Assign initial total as 0.
##2) Loop over the range from 1 to 999
##3) if any number is divisible by 3 or 5
##4) Add that number to the total
##5) Finally, print the total number

