arr = [-3,0,1,-3,1,1,1,-3,10,0]
d = {}
for i in arr:
    if i not in d:
        d[i] = 0
    d[i] += 1
lst = [d[i] for i in d.keys()]
lst2 = list(set(lst))
if len(lst) == len(lst2):
    print('True')
else:
    print('False')


