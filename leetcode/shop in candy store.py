def candyStore(self, candies, N, K):
    # code here
    min_, max_, i, j, n = 0, 0, 0, N - 1, N
    candies.sort()
    while i < n and n >= 0:
        min_ += candies[i]
        n -= K
        i += 1
    i = 0
    while j >= i:
        max_ += candies[j]
        i += K
        j -= 1
    return min_, max_