# Largest prime factor

# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def highestPrimeFactor(n):
    leftOver = n
    divisor = 2
    while divisor < leftOver:
        if leftOver % divisor == 0:
            leftOver = leftOver // divisor
        else:
            divisor += 1
    return divisor

print(highestPrimeFactor(600851475143))

# Correct answer is 6857