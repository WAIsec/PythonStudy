# 사용할 알고리즘 = 깊이 우선 탐색(Depth First Search, DFS)
#--------------------------------------------------------
# 전처리기

# show table
def ShowTable(table, size):
    print("table---------------")
    for i in range(size):
        print(table[i])
        
# MakeTable
def MakeTable(size):

    # size에 따른 N*N 행렬 생성
    table = [list(map(int, input())) for _ in range(size)]

    # print(table)
    return table    

# FindGroup(= DFS)
def FindGroup(x, y, table, verify):
    
        table[x][y] = 0 # visited 이거나 건물 없음
        
        verify.append((x,y))
        
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        
        for i in range(4):
            # size(col)를 벗어나면 안됨 and 옆(우) Index 확인
            u, v = x + dx[i], y + dy[i]
            if 0 <= u < len(table) and 0 <= v < len(table):
                # '1'인 경우
                if table[u][v] == 1:
                    # FindGroup 재귀
                    FindGroup(u, v, table, verify)

# main
def main():
    # size 입력
    size = int(input())
    
    # MakeTable
    table = MakeTable(size)

    # Array 생성 <- GroupList의 길이 값들 저장
    Array = []

    # 전체 Index 순회
    for i in range (size):
        for j in range(size):
        # Verify 배열 생성 <- FindGroup에서 반환하는 배열이 있는 경우 받을 그릇
            Verify = []    
        # FindGroup 수행
            # '0' 인 경우 '0'로 변경
            if table[i][j] == 0:
                continue
            # '1'을 발견 시 해당 Index(아파트 위치)를 Group(단지)의 시작에 배치
            elif table[i][j] == 1:
                FindGroup(i, j, table, Verify)
                
            if len(Verify):
                Array.append(len(Verify)) # 단지의 아파트 수를 저장
                # ShowTable(table, size)
                # print()
    
    # print(Array)    
    # Array 정렬
    Array.sort()
    # Array 원소 개수 출력 = 단지 개수
    print(len(Array))
    # Array 출력
    for i in range(len(Array)):
        print(Array[i])

# main() 실행
main()