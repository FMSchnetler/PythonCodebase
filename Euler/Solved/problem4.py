# Largest palindrome product

# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isNumberPalindrome(n):
    palindrome = str(n)
    if palindrome == palindrome[::-1]:
        return True
    return False

x = 999
y = x
biggestPalindrome = 1
while x > 99:
    product = x * y
    if isNumberPalindrome(product) and product > biggestPalindrome:
        biggestPalindrome = product
        x -= 1
        y = x
        if (x < biggestPalindrome ** 0.5):
            break
    else:
        if y > 99:
            y -= 1
        else: 
            x -= 1
            y = x

print(biggestPalindrome)

# Correct answer is 906609