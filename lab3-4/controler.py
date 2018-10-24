from math import sqrt

#*******check_functions********

def check_start_and_end(my_list, start, stop):
    """Checks if start and stop are valid values"""

    if start > stop:
        print("Error, start greater than end")
        return False
    if start < 0:
        print("Error, start is less than 0")
        return False
    if stop >= len(my_list):
        print("Error, end point is greater than the length of the list.")
        return False
    return True


def check_val(x,type):
    try:
        x=type(x)
        return True
    except ValueError:
        return False

#***********add_insert****************

def add_number(my_list, complex_nb):
    """This function adds a complex number at the end of the list"""

    real_nb = complex_nb.real
    imag_nb = complex_nb.imag

    my_list.append([real_nb, imag_nb])
    """print("The number was added!")"""

def insert_number(my_list,complex_nb,poz):
    """This function inserts a specific complex number at a given position"""

    real_nb = complex_nb.real
    imag_nb = complex_nb.imag

    if poz >= 0:
        my_list.insert(poz, [real_nb, imag_nb])

#***********remove_replace**********

def remove_position(my_list, poz):
    """This funtion deletes the element on position: Position"""

    if poz > len(my_list) or poz < 0:
        print("Invalid value for the position")
    else:
        del my_list[poz]
        print("The element was deleted!")


def remove_items(my_list, start_poz, end_poz):
    """This function deletes elements in range StartPoint, Endpoint"""

    if check_start_and_end(my_list, start_poz, end_poz):
        for i in range(start_poz, end_poz + 1):
            del my_list[start_poz]
        print("It worked")


def replace_item_range(my_list, old_nb, new_nb):
    """This function replaces a given number InitialNumber with a new one NewNumber"""

    for i in range(len(my_list)):
        if my_list[i][0] == old_nb.real and my_list[i][1] == old_nb.imag:
            my_list[i][0] = new_nb.real
            my_list[i][1] = new_nb.imag


#**********print_functions**********

def print_elem(x):
    if x[1] == 0:
        print(x[0])
    elif x[0] == 0:
        print(str(x[1]), 'i')
    elif x[1] > 0:
        print(str(x[0]), "+", str(x[1]), 'i')
    else:
        print(str(x[0]), "+", str(x[1]), 'i')


def print_list(List):
    """This function prints the list"""

    for i in range(0, len(List)):
        print_elem(List[i])


def print_real_nbs(List, start_poz, end_poz):
    """This function prints only the real numbers"""

    if check_start_and_end(List, start_poz, end_poz):
        for i in range(start_poz, end_poz + 1):
            if List[i][1] == 0:
                print(List[i][0], " ")


def print_numbers_modulo(List, Operator, ModuloNumber):
    """ This function prints all the numbers that
        respect this condition. The function contains a dictionary with all the possible
        values of the operator"""

    op = {'<': '__lt__', '>': '__gt__', '<=': '__le__', '>=': '__ge__', '=': '__eq__'}
    if Operator in op:
        for i in range(0, len(List)):
            if getattr(abs(sqrt(List[i][0] ** 2 + List[i][1] ** 2)), op[Operator])(ModuloNumber):
                print_elem(List[i])
    else:
        print("Invalid operator")


#**********sum_prod**************
def sum_nbs(my_list, start_poz, end_poz):
    sume = 0
    if check_start_and_end(my_list, start_poz, end_poz):
        for i in range(start_poz, end_poz + 1):
            sume += complex(my_list[i][0], my_list[i][1])
    print(complex(sume))


def prod_nbs(my_list, start_poz, end_poz):
    Prod = 1
    if check_start_and_end(my_list, start_poz, end_poz):
        for i in range(start_poz, end_poz):
            Prod *= complex(my_list[i][0], my_list[i][1])
    print(complex(Prod))


#**************filter_real**************

def filter_real(my_list):
    i = 0
    while i < len(my_list):
        if my_list[i][1] != 0:
            del my_list[i]
            i -= 1
        i += 1
    print("The elements were successfully filtered!")


def filter_modulo(List,Operator,ModuloNumber):
    op = {'<': '__lt__', '>': '__gt__', '<=': '__le__', '>=': '__ge__', '=': '__eq__'}
    if Operator in op:
        i = 0
        while (i < len(List)):
            if not (getattr(abs(sqrt(List[i][0] * List[i][0] + List[i][1] * List[i][1])), op[Operator])(ModuloNumber)):
                del List[i]
                i -= 1
            i += 1
        print("The numbers were successfully filtered!")
    else:
        print("Invalid operator!")