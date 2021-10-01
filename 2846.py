N = int(input())
Pi = list(map(int, input().split()))

max_Pi = 0
init_up = -1

for i in range(N+1):
    if i == 0:
        init_up = Pi[i]
    else:
        if Pi[i] > Pi[i-1]:
            if init_up == -1:
                init_up = Pi[i-1]
            else:
                if Pi[i]-init_up >= max_Pi:
                    max_Pi = Pi[i]-init_up
        else:
            init_up = -1

print(max_Pi)
