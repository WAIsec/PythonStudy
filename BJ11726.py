# 문제: 117266 백준 2*n 타일
# 작성자: 이인혁
# 알고리즘 분류: DP
# --------------
import sys; input = sys.stdin.readline

# main 정의
def main():
    tile = int(input())
    
    d = [0] * (1001) 
    
    # 타일이 1개 일 때 경우의 수 1
    d[1] = 1
    
    # 타일이 2개 일 때 경우의 수 2
    d[2] = 2
    
    for i in range(3, 1001):
        d[i] = d[i-1] + d[i-2]
    
    # 마지막 타일의 경우의 수 출력
    print(d[tile] % 10007) # 문제 조건
    
# main함수 호출
main()