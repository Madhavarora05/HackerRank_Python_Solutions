def minion_game(string):
    s_length = len(string)
    vowel_list = ["A", "E", "I", "O", "U"]
    stuart_point = 0
    kevin_point = 0
    for i in range(s_length):
        if string[i] in vowel_list:
            kevin_point += s_length - i
        else:
            stuart_point += s_length - i
    if stuart_point == kevin_point:
        print("Draw")
    elif kevin_point > stuart_point:
        print("Kevin", kevin_point)
    else:
        print("Stuart", stuart_point)

if __name__ == '__main__':
    s = input()
    minion_game(s)