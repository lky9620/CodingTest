N = int(input())
ls_N = list(map(int,input().split()))
cnt_i = 0
cnt_j = 0
for i in range(N):
    for j in range(1, ls_N[i]+1):
        if ls_N[i]%j == 0:
            cnt_j += 1
    if cnt_j == 2:
        cnt_i += 1
    cnt_j = 0


print(cnt_i)