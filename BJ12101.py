import sys; input = sys.stdin.readline

# printFunction() def
def printFunction(n, k, d):
    
    if n <= 0:
        print("")
        return
    
    if 0 < k <= d[n][1]:
        print("+", end="")
        print(1,end="")
        printFunction(n-1, k, d)
    elif k <= d[n][1]+d[n][2]:
        print("+", end="")
        print(2,end="")
        k -= d[n][1] 
        printFunction(n-2, k, d)
    elif k <= d[n][1]+d[n][2]+d[n][3]:
        print("+", end="")
        print(3,end="")
        k -= d[n][1] + d[n][2]
        printFunction(n-3, k, d)
    else:
        print("")
        return

def main():
    n, k = map(int, input().split())
    d = [[0] * 4 for _ in range(n+1)]
    
    if n >= 1:
        # d[1][] 설정
        d[1][1] = 1
        d[1][2] = 0
        d[1][3] = 0
    
    if n >= 2:
        # d[2][] 설정
        d[2][1] = 1
        d[2][2] = 1
        d[2][3] = 0
    
    if n >= 3:
        # d[3][] 설정
        d[3][1] = 2
        d[3][2] = 1
        d[3][3] = 1
    
    for i in range (4, n + 1):
        d[i][1] = d[i-1][1] + d[i-1][2] + d[i-1][3]
        d[i][2] = d[i-2][1] + d[i-2][2] + d[i-2][3]
        d[i][3] = d[i-3][1] + d[i-3][2] + d[i-3][3]
    
    val = 0
    if 0 < k <= d[n][1]:
        print(1,end="")
        val=1
    elif k <= d[n][1]+d[n][2]:
        print(2,end="")
        k -= d[n][1]
        val=2
    elif k <= d[n][1]+d[n][2]+d[n][3]:
        print(3,end="")
        k -= d[n][1]+d[n][2]
        val=3
    else:
        print(-1)
        return
    
    printFunction(n-val, k, d)

# main 함수 실행
main()