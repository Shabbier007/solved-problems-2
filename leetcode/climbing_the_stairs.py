def climbine(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    t = [1, 1]
    for i in range(2, n+1):
        t.append(t[i-1] + t[i-2])
    return t[n]