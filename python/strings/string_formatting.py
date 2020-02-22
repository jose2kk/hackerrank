def print_formatted(number):
    w = len(str(bin(n)[2:]))
    for i in range(1, n + 1):
        print(str(i).rjust(w, ' '), str(oct(i))[2:].rjust(w, ' '), 
        str(hex(i))[2:].title().rjust(w, ' '), str(bin(i))[2:].rjust(w, ' '))