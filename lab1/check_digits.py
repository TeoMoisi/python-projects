def check_Digits(nr1, nr2):
    """
    Verifies if two numbers have at least 2 common digits
    n1: first number
    n2: second number
    returns true if they have at least 2 common digits.
    """

    n1 = [0] * 10
    n2 = [0] * 10

    while nr1 > 0:
        n1[nr1 % 10] = 1
        nr1 //= 10

    while nr2 > 0:
        n2[nr2 % 10] = 1
        nr2 //= 10

    counter = 0

    for i in range(0, 10):
        if n1[i] == n2[i] == 1:
            counter += 1

    return counter >= 2

def checkP3(numbers):
    """
    Checks if all consecutive number pairs have at least 2 common digits 
    :param numbers: the list that needs to be verified
    :return: true if the condition from above is aquired, false if not
    """
    for i in range(0, len(numbers) - 1):
        if not check_Digits(numbers[i], numbers[i+1]):
            long += 1
        else:
            long = 0
        if long > maxim:
            maxim = long
            start = i - long + 1
    for i in range(maxim):
        print(numbers[i + start])
