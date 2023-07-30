# 그룹 단어 체커
'''
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.

입력1
3
happy
new
year

결과1
3


입력2
4
aba
abab
abcabc
a

결과2
1
'''

# 준비단계
num = int(input())
str_list = []
for i in range(num):
    str_list.append(input())

# 확인단계
storage = []
cnt = 0
prev_char = ''
for string in str_list:
    temp_list = list(string)

    for idx, char in enumerate(temp_list):
        if prev_char != char:
            prev_char = char
            if char not in storage:
                storage.append(char)
            else:
                prev_char = ''
                storage = []
                break
        if idx == len(temp_list) -1:
            prev_char = ''
            cnt += 1
            storage = []

print(cnt)