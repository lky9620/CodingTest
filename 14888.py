N = int(input())
A = list(map(int, input().split()))
OP = list(map(int, input().split()))
max_N = 0
min_N = 0
OP_N = 0

def factorial(N):
    fact_N  = 1
    for i in range(1,N+1):
        fact_N *=i
    return fact_N

for i in range(len(OP)):
    if OP[i] != 0:
        OP_N +=1

for i in range(OP_N**((N-1)-(OP_N-1))*factorial(OP_N-1)):
    A[i]