# 백준 7567 토마토 문제
#-------------------------------------------
# 전처리기
from collections import deque

false = 0
true = 1

# showBoxTable 함수 def
def showBoxTable(boxTable):
    print("---Box-Status---")
    for i in range(len(boxTable)):
        for j in range(len(boxTable[0])):
            print('%2d' % boxTable[i][j], end=" ")
        print()

# maxValue 함수 def
def maxValue(boxTable):
    max = 0
    
    for i in range(len(boxTable)):
        for j in range(len(boxTable[0])):
            if max < boxTable[i][j]:
                max = boxTable[i][j]
    
    return max

# detectRawTomato 함수 def
def detectRawTomato(boxTable):
    for i in range(len(boxTable)):
        for j in range(len(boxTable[0])):
            if not(boxTable[i][j]): # 익지 않은 토마토가 있다!
                return true
    
    return false # 없다!

# createBox 함수 def
def createBox():
    col, row = map(int, input().split())
    
    boxTable = [list(map(int, input().split())) for _ in range(row)]
    
    return boxTable

# dayCounter 함수 def = BFS
def dayCounter(boxTable):
    
    # 좌표 담을 큐 생성
    q = deque([])
    
    # 범위 생성
    col_r = len(boxTable[0])
    row_r = len(boxTable) 
    
    for i in range(len(boxTable)):
        for j in range(len(boxTable[0])):
            if boxTable[i][j] == 1:
                q.append((i, j))

    dx = [-1, 1, 0, 0] # 좌, 우
    dy = [0, 0, -1, 1] # 하, 상.
    
    while q: 
        row, col = q.popleft()

        for i in range(4):
            u = row + dy[i]
            v = col + dx[i]
            
            # 범위 내에 있어야함
            if 0 <= u < row_r and 0 <= v < col_r and boxTable[u][v] == 0:
                boxTable[u][v] = boxTable[row][col] + 1
                q.append((u,v))
        
            # showBoxTable(boxTable)
            


# main 함수 def
def main():
    
    boxTable = createBox()
    
    dayCounter(boxTable)
    
    # 남은 익지 않은 토마토가 있다면
    if detectRawTomato(boxTable):
        print(-1) # 더이상 익힐 수 없음. 
    else:
        # 가장 높은 수 - 1이 최소 소요 일수
        day = maxValue(boxTable)
        print(day - 1)
# main 함수 실행
        
main()