A, B = map(int, input().split())

ls = []

cnt_i = 1

for i in range(B):
    for j in range(1,cnt_i+1):
        ls.append(cnt_i)
    cnt_i +=1
print(sum(ls[A-1:B]))