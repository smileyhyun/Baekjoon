n, m = map(int, input().split())

result = 0

for i in range(n):
    num = list(map(int, input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value = min (num)
    #가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
    
print(result)