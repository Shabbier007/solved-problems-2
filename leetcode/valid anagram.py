def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    d = {}
    for i in s:
        if i not in d:
            d[i] = 0
        d[i] += 1
    for i in t:

        if i in d:
            if d[i] > 0:
                d[i] -= 1
            else:
                return False
        else:
            return False
    return True