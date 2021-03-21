def kmp(parent, pattern):
    n = len(parent)
    m = len(pattern)
    table = [0] * m

    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    j = 0
    for i in range(n):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]
        if parent[i] == pattern[j]:
            if j == (m - 1):
                return 1
            j += 1
    return 0


s = input()
p = input()
print(kmp(s, p))
