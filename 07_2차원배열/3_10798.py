# 세로읽기
'''
총 다섯줄의 입력이 주어진다. 
각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다. 
영어 대문자 ‘A’부터 ‘Z’, 
영어 소문자 ‘a’부터 ‘z’, 
숫자 ‘0’부터 ‘9’
각 줄의 시작과 마지막에 빈칸은 없다.

예제
A A B C D D
a f z z 
0 9 1 2 1
a 8 E W g 6
P 5 h 3 k x

세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다.
다섯 번째 자리를 보면 두 번째 줄의 다섯 번째 자리의 글자는 없다. 
이런 경우처럼 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다. 
다섯 번째 자리를 세로로 읽으면 D1gk

결과 : Aa0aPAf985Bz1EhCz2W3D1gkD6x
'''
word_list = []
for num in range(5):
	word_list.append(list(input()))

result = ''
for range_idx in range(15):
	for data in word_list:
		try:
			result +=data[range_idx]
		except IndexError as e:
			pass
print(result)