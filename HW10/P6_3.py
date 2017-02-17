def reverse(n):
    r = 0
    while n > 0:
        r = (10 * r) + n % 10
        n //= 10
    return r


def isPalindrome(n):
    return n == reverse(n)

num = eval(input("Enter an integer: "))
if isPalindrome(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")