N = int(input())
# ls_N = list(range(N))

ls_N = list(map(int, input().split()))
for i in range(N):
    ls_N[i] = int(ls_N[i])

min_N = ls_N[0]
max_N = ls_N[0] 
for i in range(len(ls_N)):
    if ls_N[i] <= min_N:
        min_N = ls_N[i]
    elif ls_N[i] > max_N:
        max_N = ls_N[i]

print(min_N, max_N)