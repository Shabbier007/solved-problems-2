def getDescentPeriods(self, prices: List[int]) -> int:
    i = 0
    res = 0
    while i < len(prices):
        len_ = 1
        while i + 1 < len(prices) and (prices[i] - prices[i + 1] == 1):
            i += 1
            len_ += 1

        res += (len_ * (len_ + 1)) / 2
        i += 1
    return int(res)