# 별 찍기 - 1 성공
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	176856	108824	92181	62.560%
# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

# 예제 입력 1 
# 5

# 예제 출력 1 
# *
# **
# ***
# ****
# *****

A = int(input())

star='*'

check=0
for i in range(A):
    if check > A:
        break
    print(star*(check+1))
    check+=1
    