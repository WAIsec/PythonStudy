import sys; input = sys.stdin.readline
from collections import deque

# DFS 함수 정의
def DFS(start, vertex, dfs_check, graph):

    pos = start - 1
    print(start, end=" ")
    dfs_check[pos] = 1

    # graph 내림차순 정렬 -> 인접한 정점이 여러 개인 경우 적은 값의 정점부터 가야한다는 문제 조건 때문
    graph[pos].sort()
    for i in graph[pos]:  ## graph[vertex-1] = [4,3,2]
        if dfs_check[i] == 0 :
            DFS(i + 1, vertex, dfs_check, graph)    # 여기서 i+1을 해주지 않고 i를 해서 무한루프가 나온 것!!

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
            if check[i] == 0 and i in graph[pos]:
                q.append(i)
                check[i] = 1
                
        print(pos + 1, end=" ")  # queue에서 나오는 순서대로 탐색이기 때문에 출력

# 입력받은 값으로 그래프 그리는 함수
def Graph(edge):    
    # 전체가 vertex * vertex 크기고 0으로 채워진 graph 
    adj_list = [[] for _ in  range(edge)]

    for _ in range(edge):
        v1, v2 = map(int, input().split())
        adj_list[v1-1].append(v2-1)
        adj_list[v2-1].append(v1-1)
    
    return adj_list

# 값 입력
vertex, edge, start = map(int, input().split())
# print(vertex, edge, start) input verify

check = [0] * vertex

# graph 생성
graph = Graph(edge)
# print(graph)

#DFS 실행
dfs_check = [0] * vertex
DFS(start, vertex, dfs_check, graph)

#newline
print()

#BFS 실행
BFS(start, vertex, graph)