def reverse(n):
    r = 0
    while n > 0:
        r = (10 * r) + n % 10
        n //= 10
    return r


def isPrime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
            break
    else:
        return True


def isPalindrome(n):
    return n == reverse(n)


def isPalindronePrime(n):
    return isPrime(n) and isPalindrome(n)


def main():
    count = 0
    n = 2
    while count >= 0:
        if isPalindronePrime(n):
            count += 1
            if count % 10 == 0:
                print(format(n, "6d"), end="\n")
            else:
                print(format(n, "6d"), end=" ")
        if count == 100:
            break
        n += 1

main()
