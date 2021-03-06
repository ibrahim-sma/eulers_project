# @author : Ibrahim Sma
# @github_location: https://github.com/ibrahim-sma
# @email: ibrahim.sma1990@gmail.com
# @LinkedIn: www.linkedin.com/in/ibrahim-sma

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Problem 8 -  Largest product in a series

# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

series = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Solution:

# Assigning the maximum product of 13 adjacent digit as 1
max_prod = 1

# Looping of the values in the series until before last 13 digits as we are picking 13 values at a time
for i in range(len(series) - 13):
    
    # checking 13 values at a time and skipping if 0 is one among them
    current_values = series[i:i+13]
    if '0' in current_values:
        continue

    # This block multiply all the thirteen digits and product is assigned to curr_prod
    curr_prod = 1
    for j in current_values:
        curr_prod *= int(j)

    # If current product is greater than maximum product, maximum product is replaced with current product
    if curr_prod > max_prod:
        max_prod = curr_prod

print(max_prod)
