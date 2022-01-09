# we are doing a left shift to the mask and adding 1 in the end by using or operator
# making a right shift to the m
# taking the complement of n applying and operation to complementary n
# returning our answer


def bitwiseComplement(self, n: int) -> int:
    m = n
    mask = 0
    if n == 0:
        return 1
    while m != 0:
        mask = (mask << 1) | 1
        m = m >> 1
    ans = (~n) & mask
    return ans