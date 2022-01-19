# 체스판 다시 칠하기
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	56503	26067	21045	46.431%
# 문제
# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

# 출력
# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

# 예제 입력 1 
# 8 8
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW

# 예제 출력 1 
# 1

# 예제 입력 2 
# 10 13
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# WWWWWWWWWWBWB
# WWWWWWWWWWBWB

# 예제 출력 2 
# 12

# 예제 입력 3 
# 8 8
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB

# 예제 출력 3 
# 0

# 예제 입력 4 
# 9 23
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBW

# 예제 출력 4 
# 31

# 예제 입력 5 
# 10 10
# BBBBBBBBBB
# BBWBWBWBWB
# BWBWBWBWBB
# BBWBWBWBWB
# BWBWBWBWBB
# BBWBWBWBWB
# BWBWBWBWBB
# BBWBWBWBWB
# BWBWBWBWBB
# BBBBBBBBBB
# 예제 출력 5 
# 0

# 예제 입력 6 
# 8 8
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWWWB
# BWBWBWBW

# 예제 출력 6 
# 2

# 예제 입력 7 
# 11 12
# BWWBWWBWWBWW
# BWWBWBBWWBWW
# WBWWBWBBWWBW
# BWWBWBBWWBWW
# WBWWBWBBWWBW
# BWWBWBBWWBWW
# WBWWBWBBWWBW
# BWWBWBWWWBWW
# WBWWBWBBWWBW
# BWWBWBBWWBWW
# WBWWBWBBWWBW

# 예제 출력 7 
# 15


n, m = map(int,input().split()) # N,M 받기(n이 세로, m이 가로) 헷갈리지 말자!
mat  = [input() for _ in range(n)] # 체스판 받기

## n 과 m이 8보다 클 때는 8*8 크기로 체스판을 뽑아서 for 구문으로 돌리고 바뀌는 칸의 갯수를 세자

## 체스판을 돌리는 방법 : 만약 n=9, m=9 라면 체스판은 리스트 기준 [0:8],[1:9] 그리고 리스트 안의 값에서 [0:8][1:9] => 2*2 총 4번 계산해야함
temp=[]
for i in range(n-7): ##### 시작점을 생각하자(시작 줄) n이 9일 때 기준 리스트의 0번과 1번 인덱스를 뽑은거야... 헷갈리지 말자
    for j in range(m-7): ###### 자 이거는 가로야.. n으로 세로줄을 돌렸으니, m을 이용하여 리스트 안의 값에서 시작점을 넣어주자 할 수있어!
        ### 자 그러면 for 구문이 한 번 돌아갔다고 생각해보자 n, m = 9, 9 일 때 i는 0이야, j도 0이야 즉 첫 번째 줄의 첫 번째 값이지
        ### 그러면 두 번 돌아갔다고 생각해보자 i는 0이고 j는 1이야 즉 첫 번째 줄의 두 번째 값이지 ㅇㅋ
        ### 아니지 현재 시작점만 존재하자나 그러면 마지막 끝나는 지점도 만들어줘야지
        cntW = 0
        cntB = 0
        for q in range(i,i+8):### 이렇게 하면 시작 지점부터 총 8개줄이 생기는거지
            for p in range(j,j+8):### 자 이제 체스판을 돌리는 것 까지는 완료했어 그러면 이제 칸 하나씩을 찍어내보자 그런데 생각해보니 체스판의
                #시작점이 B냐 W나에 따라서 달라. 그런데 열과 행의 인덱스 합이 짝수끼리는 서로 같아야 하고 홀수 끼리는 서로 같아야해 ㅇㅋ 그러면
                #다를 때만 카운팅해주자
                if (q+p) %2 ==0: ## 짝수일 떄 
                    if mat[q][p] != 'W':
                        cntW += 1
                    if mat[q][p] != 'B':
                        cntB += 1
                else:
                    if mat[q][p] != 'B':
                        cntW += 1
                    if mat[q][p] != 'W':
                        cntB += 1
        temp.append(cntW)
        temp.append(cntB)

print(min(temp))

