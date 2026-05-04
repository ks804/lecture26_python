import random
limit = 50
try_limit = 7
num_try = 0


print("============== 숫자 맞추기 게임 =================")
print(f"1부터 {limit}까지의 숫자 중 ")
print(f"컴퓨터가 생각한 숫자를 {try_limit}번 안에 맞추세요")
computer_number = random.randint(1, limit)
print(computer_number)

while num_try < try_limit:
    human_number = int(input("숫자를 입력하세요 : "))
    if human_number == computer_number:
        print('human win!')
        break
    elif computer_number < human_number:
        print("down bro")
    else:
        print("up bro")

if num_try == try_limit:
    print('human lose human so ez')