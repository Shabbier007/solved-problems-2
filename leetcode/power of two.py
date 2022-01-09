# brute force approach
# we are finding the power each and every time
def isPowerOfTwo(self, n: int) -> bool:
    i = 0
    while i < 32:
        if n == 2 ** i:
            return True
        i += 1
    return False

# optimal solutions we are storing our output in an ans var
# every time we just multiplying with 2
def isPowerOfTwo(self, n: int) -> bool:
    i = 0
    ans = 1
    while i < 32:
        if n == 2 ** i:
            return True
        i += 1
        ans *= 2
    return False