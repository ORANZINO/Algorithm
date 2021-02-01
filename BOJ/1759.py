from itertools import combinations

l, c = map(int, input().split())
chars = set(input().split())
consonants = chars - set(['a', 'e', 'i', 'o', 'u'])
vowels = chars - consonants
answer = []

for i in range(l - 2):
    c_num = 2 + i
    v_num = 1 + (l - 3) - i

    for c_com in combinations(consonants, c_num):
        for v_com in combinations(vowels, v_num):
            answer.append(''.join(sorted(list(c_com) + list(v_com))))

answer.sort()

for a in answer:
    print(a)
