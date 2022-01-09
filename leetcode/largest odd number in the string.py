# the last digit of any number decides whether the whole number is even or odd
# we are checking from the last digit if we found any odd number then we are simply print the string upto that

num = "354272"
i = len(num) - 1
while i >= 0:
    if int(num[i]) % 2 == 1:
        print(num[:i+1])
        break
    i -= 1
else:
    print('not found')