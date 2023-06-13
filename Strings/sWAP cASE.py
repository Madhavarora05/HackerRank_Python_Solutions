def swap_case(sen):
    updated_str=""
    for i in sen:
        if i.islower():
            updated_str += i.upper()
        elif i.isupper():
            updated_str += i.lower()
        else:
            updated_str += i
    return updated_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)