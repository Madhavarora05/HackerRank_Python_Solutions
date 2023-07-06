def fun(s):
    try:
        username, url = s.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False
    if len(extension) > 3:
        return False
    elif website.isalnum()==0:
        return False
    if username.replace("-", "").replace("_", "").isalnum()==0:
        return False
    else:
        return True
    # return True if s is a valid email, else return False

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