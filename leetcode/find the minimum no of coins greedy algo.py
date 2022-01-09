arr = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
v = 49
res = []
for i in range(len(arr)-1, -1, -1):
    while v>= arr[i]:
        v -= arr[i]
        if v <=0:
            break
        res.append(v)
print(res)
