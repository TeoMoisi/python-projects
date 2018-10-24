def dist_val(elements):
    maxim = 1
    length = 1
    start = 0
    a = ' '
    b = ' '
    for i in range(len(elements) - 1):
        for j in range(i + 1, len(elements)):
            if elements[i] == elements[j] or elements[j] == a or elements[j] == b:
                length += 1
            elif a == ' ':
                a = elements[j]
                length += 1
            elif b == ' ':
                b = elements[j]
                length += 1
            else:
                length = 1
                a = ' '
                b = ' '
                continue
            if length > maxim:
                maxim = length
                start = i
            length = 1
            a = ' '
            b = ' '
    print_sequence(elements, start, start + maxim)
