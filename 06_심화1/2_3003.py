#  킹, 퀸, 룩, 비숍, 나이트, 폰
regular = [1,1,2,2,2,8]
input = list(map(int, input().split()))
result = []

for idx, num in enumerate(input):
	result.append(regular[idx] - num)

print(*result)
