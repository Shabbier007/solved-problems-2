# 1st approach by using power set algorithm

# Time comp O(2**n) O(2**n)

N = 3
arr = [5, 2, 1]
sum_sub = []
for i in range(2**N):
    res = ''
    j = 0
    while i != 0:
        bit = i&1
        if bit:
            res += str(arr[j])
        i = i>>1
        j += 1
    if res == '':
        sum = 0

    sum = 0
    for j in res:
        sum += int(j)
    sum_sub.append(sum)
sum_ = 0

sum_sub = list(set(sum_sub))
print(sum_sub)

