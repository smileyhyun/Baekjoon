#배열의 크기 n, 숫자가 더해지는 횟수 m, 특정 수 연속해서 몇번 k
#N,M,K를 공백으로 구분하여 입력받기
n,m,k= map(int, input().split())
#N개의 수를 공백으로 구분하여 입력받기
num = list(map(int, input().split()))

num.sort()
first = num[n-1]
second=num[n-2]
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m ==0:
        break
    result += second
    m -= 1
    
print(result)