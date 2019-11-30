# Smallest multiple

# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n = 1
while True:
    x = 1
    while x < 11:
        if n % x != 0:
            break
        x += 1
    n += 1
