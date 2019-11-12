from functools import lru_cache

def recursiveFibonnaci5(n: int) -> int:
    if n == 0:
        return n
    last = 0
    next = 1
    for _ in range(1, n):
        (last, next) = (next, last + next)
    return next

@lru_cache(maxsize=None)
def recursiveFibonnaci4(n: int) -> int:
    if n < 2:
        return n
    return recursiveFibonnaci4(n-1) + recursiveFibonnaci4(n-2)

memo = {0: 0, 1: 1}
def recursiveFibonnaci3(n: int) -> int:
    #has memo
    if n not in memo:
        memo[n] = recursiveFibonnaci3(n-1) + recursiveFibonnaci3(n-2)
    return memo[n]

def recursiveFibonnaci2(n: int) -> int:
    #takes forever and wastes time getting the same answer multiple times
    if n < 2:
        return n
    return recursiveFibonnaci2(n-1) + recursiveFibonnaci2(n-2)

def recursiveFibonnaci1(n: int) -> int:
    #breaks
    return recursiveFibonnaci1(n-1) + recursiveFibonnaci1(n-2)