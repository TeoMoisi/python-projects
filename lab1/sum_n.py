def sum_n(n):
    s = 0
    for i in range(n):
        s += i
    return s

n = int(input("Enter the number: "))
s = sum_n(n)
print("the sum is " + str(s))
