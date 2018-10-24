from math import sqrt

def is_prime(n):
    """this function checks if a number is prime or not.
      If it is prime, it will show True and False otherwise"""

    if n ==  2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return  False
    return True

def find_Gol_Con(n):
    """"This function is going to generate the Goldbach's conjecture.
      If there are not valid pairs, the function will show a message."""
    k = 0
    l = []
    for i in range(2, n - 2):
        if is_prime(i):
            if is_prime(n - i):
                l.append((i, n - i))

    return l

l = find_Gol_Con(100)
if len(l) == 0:
    print("There are no such numbers")
else:
    for e in l:
        print(e)

