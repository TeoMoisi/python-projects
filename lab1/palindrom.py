def form_palindrom(n):
    p = 0
    while n != 0:
        p = n % 10 + p * 10
        n = n // 10
    return p

n = int(input("Enter the number: "))
print(form_palindrom(n))
