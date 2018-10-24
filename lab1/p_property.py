def same_digits(a, b):
    """"""
    no1 = []
    no2 = []
    while a != 0:
        if no1 != a % 10:
            no1.append(a % 10)
        a = a // 10
    while b != 0:
        if no2 != b % 10:
            no2.append(b % 10)
        b = b // 10
    no1.sort()
    no2.sort()
    
    for i in range(1, 10):
        if no1[i] == no2[i]:
            return True
        else:
            return False

m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
if same_digits(m, n):
    print("The two numbers have the P property.")
else:
    print("The two numbers don't have the P property.")
