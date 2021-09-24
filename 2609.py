n1, n2 = map(int,input().split())
max_n = max(n1, n2)

for i in range(max_n, 0, -1):
    if ((n1/i)%1 == 0) and ((n2/i)%1 == 0):
        GCD_n = i
        break
LCM_n =  n1*n2/GCD_n
print(GCD_n)
print(int(LCM_n))