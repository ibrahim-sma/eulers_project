# @author : Ibrahim Sma
# @github_location: https://github.com/ibrahim-sma
# @email: ibrahim.sma1990@gmail.com
# @LinkedIn: www.linkedin.com/in/ibrahim-sma


# Problem 2 -  Even Fibonacci numbers

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


total = 0
count = 0
i = 1
j = 2
while True:
	if j >= 4000000:
		break
	if j % 2 == 0:
		# print(f"Number {j} is a even fibonacci")
		total += j
		count += 1
	i, j = j, j + i

print(f"The sum of the even-valued fibonacci terms is : {total}")
print(f"There are {count} even-valued fibonacci terms that added to a {total}")


# ***** Solution guidelines *****

# 1) Assign initial total as 0.
	
# 2) Assigning the starting numbers for i & j as 1 & 2; i- previous number & j - current number

# 3) Ensuring the value of current number (j) doesn't exceed 4 million with if j >= 4000000.

# 4) if the current fibonacci number (j) is divisible by 2, add it to the total.

# 5) i, j = j, j + i => Assigning the previous(i) number to current number as (i=j) and 
# current number(j) to sum of previous(i) + current(j) as (j = j + i)

# 6) Finally, print the total number
