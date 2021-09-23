sum = 0
ls_sum = []
for j in range(10):
    o, i  = map(int, input().split())
    sum = sum+i-o
    ls_sum.append(sum)

print(max(ls_sum))