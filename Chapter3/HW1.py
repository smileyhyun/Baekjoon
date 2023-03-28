#모험가 수
N = int(input())

#모험가들의 공포도 list로 입력
num = list(map(int, input().split()))
num.sort()

#그룹수
result = 0

#한 그룹당 인원수
count=0

for i in num:
    count+=1
    if count >= i:
        result += 1
        count = 0

print (result)