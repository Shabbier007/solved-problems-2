def nextGreaterElement(nums1, nums2):
    d = defaultdict(lambda: -1)
    stack = []
    for v in nums2:
        while stack and v > stack[-1]:
            d[stack.pop()] = v
        stack.append(v)
    return [d[v] for v in nums1]
nums1 = [4,1,2]
nums2 = [1,3,4,2]
nextGreaterElement(nums1, nums2)