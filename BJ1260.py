from collections import deque

# DFS 함수 정의
def DFS(start, dfs_check, graph):
    pos = start - 1
    print(start, end=" ")
    dfs_check[pos] = 1
    for i in range(len(graph)):
        if graph[pos][i] == 1 and dfs_check[i] == 0 :
            DFS(i + 1, dfs_check, graph)    # 여기서 i+1을 해주지 않고 i를 해서 무한루프가 나온 것!!

# BFS 함수 정의
def BFS(start, vertex, graph):
    pos = start - 1
    q = deque()
    q.append(pos)
    check = [0] * vertex
    check[pos] = 1 # 시작하는 부분은 무조건 방문
    
    while (q):
        pos = q.popleft()
        
        for i in range(0, vertex):
            if i == pos:
                continue
            if check[i] == 0 and graph[pos][i] == 1:
                q.append(i)
                check[i] = 1
                
        print(pos + 1, end=" ")  # queue에서 나오는 순서대로 탐색이기 때문에 출력

# 입력받은 값으로 그래프 그리는 함수
def Graph(vertex, edge_list):
    
    # 전체가 vertex * vertex 크기고 0으로 채워진 graph
    graph = [[0 for col in range(vertex)] for row in range(vertex)]
    
    for i in range(len(edge_list)):
        v1, v2 = edge_list[i]
        graph[v1-1][v2-1] = 1
        graph[v2-1][v1-1] = 1

    return graph

# 값 입력
vertex, edge, start = map(int, input().split())
# print(vertex, edge, start) input verify

edge_list = []
check = [0] * vertex

for _ in range(edge):
    v1, v2 = map(int, input().split())
    edge_list.append((v1, v2))

# print(edge_list)

# graph 생성
graph = Graph(vertex, edge_list)
# print(graph)

#DFS 실행
dfs_check = [0] * vertex
DFS(start, dfs_check, graph)

#newline
print()

#BFS 실행
BFS(start, vertex, graph)