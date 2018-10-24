from math import sqrt

def is_prime(n):

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

"""this function finds Golbach Conjecture"""
"""if Golbach's Conjecture is nor possible for some numbers, it will show a message"""

def find_Gol_Con(n):
    k = 0
    for i in range(2, n-2):
        if is_prime(i):
            if is_prime(n - i):
                print("(",i,",",n - i,")")
                k = 1

    if k == 0:
        print("There are no such pairs")


if __name__ == "__main__":
        find_Gol_Con(11) 
