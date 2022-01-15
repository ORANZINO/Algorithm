import collections

# Solution 1


class MyStack:

    def __init__(self):
        self.q = collections.deque()
        self.spare = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        result = None
        while self.q:
            if len(self.q) == 1:
                result = self.q.popleft()
            else:
                self.spare.append(self.q.popleft())

        self.q, self.spare = self.spare, self.q

        return result

    def top(self) -> int:
        result = None
        while self.q:
            if len(self.q) == 1:
                result = self.q[0]
            self.spare.append(self.q.popleft())

        self.q, self.spare = self.spare, self.q

        return result

    def empty(self) -> bool:
        return False if self.q else True

"""
정직한 첫 번째 구현법. 
마지막 한 개가 남을 때까지 popleft()해버린다.
"""

# Solution 2


class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

"""
똑똑한 2번째 구현법
마지막에 append한 것을 가장 앞으로 옮기기 위해 n-1번만큼 스스로를 popleft()하고 append()한다.
거꾸로 순서가 돼있는 queue는 stack과 같이 pop이나 top이 가능!
"""

