def sum_of_div(n):
    """This function calculates and returns the sum of the divisors, including 1."""
    s = 1
    for i in range(2, n - 1):
        if n % i == 0:
            s += i
    return s

def is_perfect(n):
    """The function checks if the number is perfect or not.
      It returns True if the number is perfect and False otherwise."""
    if n == sum_of_div(n):
        return True
    else:
        return False
    return True

def smaller_perf(n):
    """Generates the first perfect number smaller that a given number n."""
    while is_perfect(n) == False:
        n -= 1
        if is_perfect(n) == True:
            return n
    
    
n = int(input("Enter the number: "))

print(int(sum_of_div(n)))

if is_perfect(n):
    print("The number is perfect")
else:
    print("The number is not perfect")
print(str(smaller_perf(n)))
