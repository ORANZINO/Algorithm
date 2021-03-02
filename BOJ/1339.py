n = int(input())
dic = {}

for _ in range(n):
    word = input().strip()
    l = len(word)
    for i in range(l):
        if word[i] not in dic:
            dic[word[i]] = 0
        dic[word[i]] += 10 ** (l - (i + 1))

val = sorted(dic.values(), reverse=True)
ans = 0
q = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for i in range(len(val)):
    ans += q[i] * val[i]

print(ans)
