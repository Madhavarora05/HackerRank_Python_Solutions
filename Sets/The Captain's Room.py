k=int(input())
room_number =list(map(int,input().split()))
room_number_set= set(room_number)
diff=(sum(room_number_set) * k) - sum(room_number)
print(diff//(k-1))



# It could be done using dictionary also.

# n = int(input())
# dic = {} 
# for x in input().split():
#   dic[x] = dic.get(x,0) + 1
# for key in dic:
#   if dic[key] != n: 
#     print(key)
#     break