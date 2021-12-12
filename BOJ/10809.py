s = input()
for i in range(ord('a'), ord('z') + 1):
    print(s.find(chr(i)), end=' ')


"""
a부터 z까지의 알파벳에 대해 주어진 string에서 find를 적용하면 풀 수 있는 문제
"""