def count_substring(string, sub_string):
    total = 0
    for i in range(len(string)):
        if string[i:len(string)].startswith(sub_string):
            total += 1
    return total

# Alternative solution
# def count_substring(string, sub_string):
#     counting = 0
#     while sub_string in string:
#         a=string.find(sub_string)
#         string=string[a+1:]
#         counting += 1
#     return counting

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)