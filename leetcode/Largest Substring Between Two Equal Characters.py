# o(n2) approach

s = 'dd'
len1_ = -1
max_ = len1_
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            len1_ = len(s[i+1:j])
        if len1_ > max_:
            max_ = len1_
print(max_)


# time complexity O(n) and space complexity O(n)

d = {}
max_, len_ = -1, -1
for i in range(len(s)):
    if s[i] not in d:
        d[s[i]] = i
    else:
        len_ = i - d[s[i]]-1
        if len_>max_:
            max_ = len_
print(max_)


