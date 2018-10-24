from math import sqrt

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return  False
    return True

n = int(input("Enter the value of the number: "))
if is_prime(n) == True:
    print("The number is prime")
else:
    print("The number is not prime")
