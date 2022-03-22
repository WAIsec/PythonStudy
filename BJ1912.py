# 1912번
# DP
import sys; input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
dp = [0] * n
# print(arr)
# 첫 번째 값 입력
dp[0] = arr[0]

for i in range(n):
    dp[i] = max(arr[i], dp[i-1]+arr[i])
    
# dp의 max 값 출력
print(dp[-1])
print(max(dp))