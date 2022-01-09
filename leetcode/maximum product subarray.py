arr = [1, 3,1,4,6,7,1]
pre_sum = 1
suf_sum = 1
max_ = 0
for i in range(len(arr)):
    if pre_sum == 0: pre_sum = 1
    if suf_sum == 0: suf_sum = 1

    pre_sum *= arr[i]
    suf_sum *= arr[i]

    max_ = max(max_, max(pre_sum, suf_sum))
print(max_)