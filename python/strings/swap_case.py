def swap_case(string):
    return ''.join([
        letter.upper() if letter == letter.lower()
        else letter.lower()
        for letter in string
        ])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)