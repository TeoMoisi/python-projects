def product_n(n):
    p = 1
    for i in range(1, n - 1):
        if n % i == 0:
            p = p * i
    return p

n = int(input("Enter the number here: "))
print("The product of the proper factors of " + str(n) + " is " + str(product_n(n)))
 
