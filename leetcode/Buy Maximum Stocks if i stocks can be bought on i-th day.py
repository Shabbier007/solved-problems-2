# we need to return maximum no of stocks we can buy with given money k
# only i stocks can buy

# create a list with prices and index
# sort the list with resp to prices
# loop through the index check the sum greater or not


arr = [10, 7, 19]
k = 45
arr1 = []
for i in range(len(arr)):
    arr1.append([arr[i], i+1])
print(arr1)
arr1.sort(key = lambda arr1:arr1[0])
print(arr1)
sum, count = 0, 0
for i in arr1:
    for j in range(i[1]):
        sum += i[0]
        if sum > k:
            print(count)
            break
        count += 1