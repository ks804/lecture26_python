n = int(input())
member_list = []

for i in range(n):
    age, name = input().split()
    member_list.append([int(age), name])

member_list.sort(key=lambda member_list: member_list[0])

for i in range(0, n):
    print(member_list[i][0], member_list[i][1])