def minion_game(string):
    stuart, kevin = 0, 0

    index = 0
    for letter in string:
        if letter in 'AEIOU':
            kevin += len(string) - index
        else:
            stuart += len(string) - index
        index += 1

    if kevin > stuart:
        print('Kevin', kevin)
    elif kevin < stuart:
        print('Stuart', stuart)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)