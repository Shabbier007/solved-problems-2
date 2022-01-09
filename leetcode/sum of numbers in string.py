str = '1abc23'
sum_, i = 0, 0
while i<len(str):
    if str[i].isdigit():
        res = ''
        while i<len(str) and str[i].isdigit():

            res += str[i]
            i += 1
            print(res)
        sum_ += int(res)
    i += 1
