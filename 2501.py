N, K  = input().split()
N = int(N)
K = int(K)

ls = []

for i in range(1,N+1):
    if N % i == 0:
        ls.append(i)

print(ls, len(ls))

if len(ls) < K:
    print(0)
else:    
    print(ls[K-1])
