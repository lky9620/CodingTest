T = int(input())
ans_T = []
for i in range(T):
    ls_T = list(map(int, input().split()))
    ls_T.sort()
    ans_T.append(ls_T[len(ls_T)-3])
for i in range(len(ans_T)):
    print(ans_T[i])