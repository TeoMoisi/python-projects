from math import sqrt

def noprime(n):
    i = 2
    if n == 2:
        return True
    elif (n <= 1) and (n % 2 == 0):
        return False
    else:
        while i < sqrt(n):
            if n % i == 0:
                return False
            i += 1

    return True

n = int(input("Enter the number: "))
if noprime(n) == True:
    print("The given number is prime")
else:
    print("The given number is not prime")
