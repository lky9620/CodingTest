N = int(input())
Pi = list(map(int, input().split()))

max_Pi = 0
ls_up = []

for i in range(N):
    # print(Pi[i])
    if i == 0:
        ls_up.append(Pi[i])
    else:
        if Pi[i] > Pi[i-1]:
            if len(ls_up) == 0:
                ls_up.append(Pi[i-1])
            ls_up.append(Pi[i])
            
            if i == N-1:
                if ls_up[-1]-ls_up[0] > max_Pi:
                    max_Pi = ls_up[-1]-ls_up[0]
        else:
            if len(ls_up) > 1:
                if ls_up[-1]-ls_up[0] > max_Pi:
                    max_Pi = ls_up[-1]-ls_up[0]
            ls_up =[]

print(max_Pi)