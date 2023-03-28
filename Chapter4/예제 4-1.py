
N = int(input())
Z = list(input().split())

x = 1
y = 1

for i in range(len(Z)):
    if Z[i] == 'D':
        a = x+1 
        if 0 < a < N+1:
            x = a
    elif Z[i] == 'U':
        a = x-1
        if 0 < a < N+1:
            x = a
    elif Z[i] == 'R':
        a = y+1
        if 0 < a < N+1:
            y = a
    else:
        a = y - 1
        if 0 < a < N+1:
            y = a  
    
print(x,y)