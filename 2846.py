N = int(input())
Pi = list(map(int, input().split()))

max_Pi = 0
init_up = -1

for i in range(N):
    if Pi[i] > Pi[i-1] or i==0:
        if init_up == -1:
            if i == 0:
                init_up = Pi[i]
            else:
                init_up = Pi[i-1]
        else:
            if Pi[i]-init_up > max_Pi:
                max_Pi = Pi[i]-init_up
    else:
        init_up = -1
if max_Pi == 0:
    print(0)
else:
    print(max_Pi)
