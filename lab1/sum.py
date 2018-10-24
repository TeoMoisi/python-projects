def sum_n(n):
s = 0
for i in range(1, n+1):
    s += i
return s

def main():
n = int(input("Enter the value: "))
print("the sum of the first" + str(n) + "numbers is: " + str(sum_n(n)))

main()

    
