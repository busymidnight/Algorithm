from string import ascii_lowercase

s = input()
d = {}
for i in ascii_lowercase:
    d[i] = -1

for str in s:
    d[str] = s.index(str)

print(*d.values())