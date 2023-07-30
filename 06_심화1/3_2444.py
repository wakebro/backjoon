# 별 찍기 - 7
input = int(input())

for num in range((2*input) - 1):
    if num + 1 <= input:
        print(' ' * (input-(num+1)), end='')
        print('*' * (num+1), end='')
        print('*' * (num))
    else:
        print(' ' * ((num+1) - input), end='')
        print('*' * ((num+1)-((num+1-input)*2)), end='')
        print('*' * ((num+1)-(1+(num+1-input)*2)))