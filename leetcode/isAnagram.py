alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = 'geeksforgeeks'
b = 'forgeeksgeeks'
for i in alpha:
    count = 0
    for j in a:
        if i == j:
            count += 1
    for k in b:
        if i == k:
            count -= 1
    if count != 0:
        print(0)
        break
print('true')