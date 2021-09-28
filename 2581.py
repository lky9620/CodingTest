M = int(input())
N = int(input())

ls = []
cnt_j = 0

for i in range(M,N+1):
    for j in range(2,i+1):
        if i%j == 0:
            cnt_j +=1
        if cnt_j >2:
            break
    if cnt_j == 1:
        ls.append(i)
    cnt_j = 0
if len(ls) == 0:
    print(-1)
else:
    print(sum(ls))
    print(ls[0])