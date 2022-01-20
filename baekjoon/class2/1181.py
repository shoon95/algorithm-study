# 단어 정렬
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	76977	31745	23624	40.289%
# 문제
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

# 출력
# 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

# 예제 입력 1 
# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours

# 예제 출력 1 
# i
# im
# it
# no
# but
# more
# wait
# wont
# yours
# cannot
# hesitate

### 단어 정렬
### 1. 중복 제거

###2. 길이 순으로 정렬 
### temp 초기값으로 text_1의 첫번째 원소를 넣자
### 두 번째 값의 길이가 temp의 원소의 길이보다 길면 뒤로 짧으면 앞으로 넣자
### 세 번째 값의 길이를 temp의 원소들과 비교하자 ... 어떻ㄱ게??? 
### 자 생각해보자 세 번째 값이 temp[0]보다 짧어 그러면 앞에다 추가 temp[0]보다 길고temp[1]보다 짧아 가운데로 가야해 그러면 이 방법은 힘들어
### dict 형식으로 가보자 모르겠고 dict 포기

### 원소들의 length를 구해서 리스트에 넣고 정렬 후 기존 단어의 길이가 해당 리스트의 원소 값과 같다면 새로운 (text_2) 리스트에 추가하자
n = int(input())

text=[]
for _ in range(n):
    word = input()
    if  word not in text:
        text.append(word)

text.sort(key=len)

temp = sorted(list(set(map(lambda n : len(n), text))))


### 같은 길이의 단어를 어떻게 하면 알파벳 순으로 정렬할 수 있을까???
### 봐바 길이가 같은 부분의 인덱스와 값을 뽑아서 그 부분을 임시 저장해놓고 임시 저장해놓고, 임시 저장 변수를 정렬시켜
### 그리고 뽑아 놓은 인덱스에 다시 넣는거야 ㅇㅋ

for i in temp:
    text2=[]
    for k in text:
        if i == len(k):
            text2.append(k)
    text2.sort()
    for j in text2:
        print(j)


