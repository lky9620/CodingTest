T = int(input())
for i in range(T):
    n = int(input())
    i = 0
    while(True):
        if n % 2 == 1:
            print(i, end=' ')
        if n == 1:
            break
        n = int(n/2)
        i +=1