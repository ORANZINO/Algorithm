from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001
parent = [-1] * 100001
parent[n] = n

if n > k:
    print(n - k)
    print(' '.join(map(str, range(n, k - 1, -1))))
elif n == k:
    print(0)
    print(n)
else:
    count = 0
    q = deque()
    q.append(n)
    visited[n] = True
    next_q = deque()

    while True:
        if not q:
            q = next_q
            count += 1
            next_q = deque()

        temp = q.popleft()

        if temp == k:
            print(count)
            result = [str(temp)]
            while parent[temp] != n:
                result.append(str(parent[temp]))
                temp = parent[temp]
            result.append(str(n))
            result.reverse()
            print(' '.join(result))
            break

        steps = [temp - 1, temp + 1, temp * 2]

        for step in steps:
            if 0 <= step <= 100000:
                if not visited[step]:
                    next_q.append(step)
                    parent[step] = temp
                    visited[step] = True