
word1 = "zzzyyy"

word2 = "iiiiii"

for i in word1:
            if abs(word1.count(i)-word2.count(i))>3:
                print('False')
                break
for j in word2:
            if abs(word1.count(j)-word2.count(j))>3:
                print('False')
                break
print('True')

