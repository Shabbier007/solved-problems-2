# first approach
# divide with two and store the remainder
# reverse the result

n = 10
res = ''
while n!= 0:
    bit = n % 2
    n = n//2
    res = str(bit) + res
print(res)
print(res[::-1])

# the bit manuplation approach
# apply and operation with 1 to the number
# then right shift the n
# store the result

n = 6
oup = ''
while n!=0:
    bit = n & 1
    oup = str(bit) + oup
    n = n>>1            # right shift
print(oup)


# Binery to decimal
dec = 0
j = len(oup) - 1
for i in range(len(oup)):
    dec += int(oup[i])*2**j
    j -= 1
print('decimal' , dec)


