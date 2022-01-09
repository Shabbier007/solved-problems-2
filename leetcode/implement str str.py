def strStr(a, b):
    if len(b) == 0:
        return 0
    for i in range(len(a) - len(b) + 1):
        if a[i:i+len(b)] == b:
            return i
    return -1