# 문제 : 연결 요소의 개수
# 작성자 : 이인혁
# 작성일 : 2022-03-04
# --------------------------------

# 전처리기
from collections import deque
import sys; input = sys.stdin.readline
# edgeList 함수 def
def adjList(vertex, edge):
    
    adj_list = [[] for _ in range(vertex + 1)]
    
    for _ in range(edge):
        v1, v2 = map(int, input().split())
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)
        
    return adj_list

# BFS 함수 def
def BFS(start, adj_list, visited):
    
    q = deque()
    q.append(start)
    
    while q:
        
        v1 = q.popleft()
        
        # 해당 vertex와 인접한 vertex 탐색
        for i in adj_list[v1]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

# main 함수 def
def main():

    vertex, edge = map(int, input().split())
    
    visited = [0] * (vertex + 1)    #   정점 방문 여부 저장하는 List
    
    adj_list = adjList(vertex, edge)  #   간선들의 정보를 입력받는 List
    
    cnt = 0         #   BFS 함수에서 반환되는 리스트의 개수 => 정답과 귀결
    
    for i in range(1, vertex + 1):
        
        if visited[i] == 0:
            visited[i] = 1
            cnt += 1
            BFS(i, adj_list, visited)
    
    print(cnt)
        
# main 함수 실행
main()