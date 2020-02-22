def count_substring(string, sub_string):
    if len(string) < len(sub_string):
        return 0
    count = 0
    for i in range(len(string)-len(sub_string) + 1):
        count += 1 if sub_string == string[i:i+len(sub_string)] else 0
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)