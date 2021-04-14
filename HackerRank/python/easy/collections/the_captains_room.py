k, arr = int(input()), list(map(int, input().split()))

myset = set(arr)
sum_set = sum(myset) * k
sum_arr = sum(arr)
difference = (sum_set - sum_arr)
captain = difference // (k - 1)
print(captain)

"""
#TIME_OUT
len_group = int(input())
list_room_groups = input().split()
set_room_groups = set(list_room_groups)
for x in set_room_groups:
    list_room_groups.remove(*set_room_groups)
set_room_groups_without_captain = set(list_room_groups)
print(*set_room_groups.difference(set_room_groups_without_captain))
"""
