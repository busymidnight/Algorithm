n = int(input())
cnt = n
li = []
for _ in range(n):
    words = input()
    li.append(words[0])
    for i in range(1,len(words)):
        if words[i-1] != words[i]:
                if words[i] not in li:
                        li.append(words[i])
                else:
                        cnt -= 1
                        break
    li.clear()
print(cnt)
