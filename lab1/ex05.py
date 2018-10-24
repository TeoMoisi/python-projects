from math import sqrt

def n_is_prime(n):

    """Checks if an integer number n is prime.
    n - integer
    The function returns True if the number is prime
    and it returns False otherwise."""
    
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return  False
    return True

def first_nb_prime(n):

    """Generates the first prime number smaller that a given number n."""
    while n > 0:
        n -= 1
        if n_is_prime(n):
            return n

n = int(input("Enter the value of the number: "))
print("The first prime number smaller than " + str(n) + " is " + str(first_nb_prime(n)))
