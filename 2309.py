ls_k = []
for i in range(9):
    k = int(input())
    ls_k.append(k)
for i in range(len(ls_k)):
    for j in range(i+1,len(ls_k)):
        sum_k = 0
        if i!=j:
            sum_k = ls_k[i]+ls_k[j]
            if sum(ls_k)-sum_k == 100:
                ls_k[i] = 0
                ls_k[j] = 0
                ls_k.sort()
                for i in range(2,len(ls_k)):
                    print(ls_k[i])
