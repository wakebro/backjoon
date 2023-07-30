# 최댓값

'''
같이 9x9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성
'''
total = []
for row in range(9):
    total.append(list(map(int, input().split())))
    
max = None
row = None
column = None
for r_idx, r in enumerate(total):
    for c_idx, c in enumerate(r):
        # print(r[idx])
        if max == None or c > max:
            max = r[c_idx]
            row = r_idx + 1
            column = c_idx + 1

# print(f'max : {max}')
# print(f'row : {row}, column : {column}')
print(max)
print(row, column)