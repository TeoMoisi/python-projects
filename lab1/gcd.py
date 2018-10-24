def gcm1(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    n = b
    return n

def gcm2(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    n = a
    return n


a = int(input("The first number is: "))
b = int(input("The second number is: "))
p = gcm1(a, b)
q = gcm2(a, b)
print("The greatest common divisor is: " + str(p))
print("The greatest common divisor is: " + str(q))


 
