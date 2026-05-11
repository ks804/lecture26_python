import random

word_list = ['APPLE', 'BANANA', 'MAN', 'WOMAN', 'TOMATO']
def selcet_word():
    word_list = ['APPLE', 'BANANA', 'MAN', 'WOMAN', 'TOMATO']
    return random.choice(word_list)
try_num = 0
limit_error = 7
target_word = selcet_word()
#print(">> 컴퓨터가 생각한 단어 : ", target_word)
blank_char = '_'
word_screen = blank_char * len(target_word)
num_error = 0

check = set()

while num_error < limit_error:
    user_input = input(">> 알파벳 입력 : ").upper()
    if user_input in check:
        print('중복입니다')
        continue
    check.add(user_input)

    if target_word.find(user_input) == -1:
        num_error += 1
        print(f"오답 : {num_error}회")
    else:
        for i in range(len(target_word)):
            if target_word[i] == user_input:
                word_screen = word_screen[:i] + user_input + word_screen[i+1:]
                print('정답 : ', word_screen)
    if word_screen.count(blank_char) == 0:
        print('You win!')
        break

if num_error >= limit_error:
    print('You lose :', target_word)




    
