num = list(map(int, input().split()))

#0이 바뀔 횟수
count0=0
#1이 바뀔 횟수
count1=0

if num[0] == 1:
    count1+=1
else:
    count0+=1

for i in range(len(num)-1):
    if num[i] != num[i+1]:
        if num[i+1] == 0:
            count0 += 1
        else:
            count1 += 1

print(count0,count1)
print(min(count0, count1))

#if count0<count1:
#    print(count0)
#else:
#    print(count1)


#count = 0
#for i in range(1,len(num)):
#    if num[i]==num[i+1] :
#        count = count
#    else:
#       num[i+1]=num[i]
#        count = count+2

#print(count)