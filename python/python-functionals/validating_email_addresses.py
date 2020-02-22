import re

def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, website_with_extension = s.split('@')
        website, extension = website_with_extension.split('.')
    except:
        return False

    if re.search(r'[^\w\-]', username) or len(extension) < 0 or len(extension) > 3 or len(username) == 0:
        return False
    return not bool(re.search(r'[^a-zA-Z0-9]', website))
    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)