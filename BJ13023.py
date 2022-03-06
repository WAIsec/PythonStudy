# 백준 13023 번 문제  - 'ABCDE'
# 작성자 - 이인혁
# 작성일 - 2022-03-05
# ---------------------------------
# 전처리기
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 전역변수
result = 0

# makeAdjList 함수 def
def makeAdjList(vertex, edge):
    
    ret = [[] for _ in range(vertex)]
    
    for _ in range(edge):
        v1, v2 = map(int, input().split())
        ret[v1].append(v2)
        ret[v2].append(v1)
        
    return ret

# DFS 함수 def
def DFS(vertex, cont_rel, visited, adjList):
    global result
    if cont_rel == 4:
        result = 1
        return
    
    for i in adjList[vertex]:
        if visited[i] == 0:
            visited[i] = 1
            DFS(i, cont_rel+1, visited, adjList)
            visited[i] = 0 

# main 함수 def
def main():
    
    vertex, edge = map(int, input().split())
    adjList = makeAdjList(vertex, edge)
    
    visited = [0] * vertex
    
    for i in range(vertex):
        if visited[i] == 0:
            visited[i] = 1
            DFS(i, 0, visited, adjList)
            visited[i] = 0
        if result:
            break
    
    if result:
        print(result)
    else:
        print(result)
    
# main 함수 실행
main()