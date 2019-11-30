count = 4
nextPrime = 9
maybePrime = 7
divisor = 3

while count <= 10:
    if maybePrime % divisor != 0:
        if divisor < maybePrime / 2:
            divisor += 2
        else:
            count += 1
            maybePrime += 2
            divisor = 3
            print(maybePrime)
            continue
    else:
        maybePrime += 2
        divisor = 3

print(maybePrime-2)
        