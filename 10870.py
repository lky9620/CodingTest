n = int(input())
ls_n = []
for i in range(n+1):
    if i == 0:
        ls_n.append(0)
    elif i == 1:
        ls_n.append(1)
    else:
        ls_n.append(ls_n[i-1]+ls_n[i-2])

print(ls_n[-1])