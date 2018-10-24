import sys
from math import sqrt

def read_list(list_n):
    n = int(input("Introduce the number of the elements: "))
    print("The numbers are: ")
    for i in range(0, n):
        x = int(input())
        list_n.append(x)
    return list_n

def print_funct(list_n, start_poz, end_poz):
    if start_poz == 0 and end_poz == len(list_n) :
        print ("The elements of the list are: ")
    else :
        print("This is the longest sequence which has the given property : ")
    for i in range (start_poz, end_poz):
        print(list_n[i])

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

def long_prime(list_n):

    maxim = 0
    start_poz = -1
    end_poz = -1
    for i in range (len(list_n)-1):
        if is_prime(list_n[i]) == 1: 
            l = 1   
            ok = 1
            stop = i + 1
            for j in range (i+1,len(list_n)-1): 
                if ok == 1:
                    if is_prime(list_n[j]) == 1:
                        l += 1
                        stop = j + 1
                    else:
                        ok = 0
            if maxim < l :
                maxim = l
                start_poz = i
                end_poz = stop
    if start_poz != -1 :
        print_funct(list_n, start_poz, end_poz + 1)
    else :
        print("There is not such a sequence!")

def strict_incr(list_n):
    maxim = 0
    start_poz = -1
    end_poz= -1
    last_elem = 0
    for i in range (len(list_n)-1):
        l = 1
        ok = 1
        stop = i + 1
        last_elem = list_n[i]
        for j in range (i+1,len(list_n)):
            if ok == 1 :
                if last_elem < list_n[j] :
                    l += 1
                    last_elem = list_n[j]
                    stop = j + 1
                else :
                    ok = 0
            if maxim < l :
                maxim = l
                start_poz = i
                end_poz = stop
    print_funct(list_n, start_poz, end_poz)


def in_range(list_n):
    """This function checks which numbers are in [0, 10] and prints out the
    longest sequence which satisfies this property."""
    maxim = 0
    length = 0
    for i in range(0, len(list_n)):
        if list_n[i] > 0 and list_n[i] < 10:
            length +=1
        else:
            length = 0
        if length > maxim:
            maxim = length
            begin = i - length + 1
    """for i in range(maxim):
        print(elements[i + begin])"""
    print_funct(list_n, begin, begin + maxim)

def single_nb(list_n):
    maxim = 0
    start_poz = -1
    end_poz = -1
    for i in range (len(list_n)-1):
        l = 1
        element = list_n[i]
        ok = 1
        stop = i + 1
        for j in range (i+1,len(list_n)):
            if ok == 1 :
                if list_n[j] == element :
                    l+=1
                    last_elem = list_n[j]
                    stop = j + 1
                else:
                    ok = 0
            if maxim < l :
                maxim = l
                start_poz = i
                end_poz = stop
    
    return list_n, start_poz, end_poz

def exit_funct(list_n):
    sys.exit()

def menu_options():
    print("0. Exit")
    print("1. Help")
    print("2. Read the list")
    print("3. Print the list")
    print("4. Print the longest sequence which contains only prime numbers")
    print("5. Print the longest sequence which contains only increasing numbers")
    print("6. Print the longest sequence which contains only numbers in range [0, 10]")
    print("7. Print the longest sequence which contains only one number.")

def main():
    print("\n\t Welcome to my app! For more information press 1!")
    list_n = [1, 2, 4,2, 5, 6, 7, 1, 2,3, 4, 5]
    while True:
        opt = int(input("Input an option: "))
        if opt == 1:
            menu_options()
        if opt == 2:
            read_list(list_n)
        if opt == 3:
            print_funct(list_n, 0, len(list_n))
        if opt == 4:
            long_prime(list_n)
        if opt == 5:
            strict_incr(list_n)
        if opt == 6:
            in_range(list_n)
        if opt == 7:
            a, b, c = single_nb(list_n)
            print_funct(a, b, c)
        if opt == 0:
            exit_funct(list_n)
          
          
main()
