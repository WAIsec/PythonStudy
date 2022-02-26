import sys; input = sys.stdin.readline
from collections import deque

# 전체 타일 개수 입력
TileTotal = int(input())
# 전체 타일 값 입력
TileValue = list(map(int,input().split()))

# 시작 노드 입력
q = deque([(0, TileValue[0])])


# 방문한 노드 체크를 위한 배열
check = [0] * TileTotal

# TileTotal 값이 1일 경우
if TileTotal == 1:
    print(0)
    sys.exit()
    
# 비교 시작
while q:
    current, jmp = q.popleft() # 0, 1
    
    for j in range(1, jmp + 1):
        if current + j < TileTotal and check[current + j] == 0:
            q.append((current + j, TileValue[current + j]))
            check[current + j] = check[current] + 1
    # 모든 타일을 이동해도 끝에 도달하지 못한다면 -1 출력

if check[-1]:
    print(check[-1])
else:
    print(-1)