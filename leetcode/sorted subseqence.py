a = [33, 24, 92, 74, 100, 72, 72, 97, 54, 77, 95, 52, 11, 95, 29]
a.sort()
print(a)
d = {}
for i in range(len(a)):
    if i not in d:
        d[a[i]] = i
    d[a[i]] += 1
res = []
for i in range(len(a)):
    if a[i]-1 in d and a[i]-2 in d and d[i-1]<i and d[i-2]<i and d[i] :
        res.append([i-2, i-1, i])
        break
print(res)