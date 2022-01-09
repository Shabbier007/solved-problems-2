# we need to find the weight of each point
# arrange the single weights in descending order
#
# time complexity is Nlogn + n  and O(1)

def fractionalknapsack(self, W, Items, n):
    arr = []
    for i in range(n):
        arr.append([Items[i].value, Items[i].weight, Items[i].value / Items[i].weight])
    arr.sort(key=lambda arr: arr[2], reverse=True)
    currWeight, finalV = 0, 0
    for i in range(len(arr)):
        if currWeight + arr[i][1] <= W:
            currWeight += arr[i][1]
            finalV += arr[i][0]
        else:                                   # when the knaspack is full
            rem = W - currWeight
            finalV += rem * arr[i][2]
            break

    return finalV