sumSquares = 0
sum = 0

x = 1
while x <= 100:
    sumSquares += x**2
    sum += x
    x += 1

print(sum**2 - sumSquares)