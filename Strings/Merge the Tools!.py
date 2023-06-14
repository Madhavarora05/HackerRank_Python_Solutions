from collections import OrderedDict
def merge_the_tools(string, k):
    i = 0
    while i < len(string):
        word1 = "".join(OrderedDict.fromkeys(string[i: i+k]))      
        print(word1)
        i = i + k
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)