from bisect import bisect_left, bisect_right

arr = [[] for _ in range(10001)]
reversed_arr = [[] for _ in range(10001)]


def count_by_range(query):
    if query[0] != '?':
        left, right = query.replace('?', 'a'), query.replace('?', 'z')
        return bisect_right(arr[len(query)], right) - bisect_left(arr[len(query)], left)
    else:
        query = query[::-1]
        left, right = query.replace('?', 'a'), query.replace('?', 'z')
        return bisect_right(reversed_arr[len(query)], right) - bisect_left(reversed_arr[len(query)], left)


def solution(words, queries):
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])

    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()

    return [count_by_range(q) for q in queries]

