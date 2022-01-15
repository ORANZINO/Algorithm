# Solution 1
class MyQueue:

    def __init__(self):
        self.stack, self.spare = [], []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for _ in range(len(self.stack) - 1):
            self.spare.append(self.stack.pop())
        result = self.stack.pop()
        while self.spare:
            self.stack.append(self.spare.pop())
        return result

    def peek(self) -> int:
        for _ in range(len(self.stack) - 1):
            self.spare.append(self.stack.pop())
        result = self.stack.pop()
        self.spare.append(result)
        while self.spare:
            self.stack.append(self.spare.pop())
        return result

    def empty(self) -> bool:
        return len(self.stack) == 0


"""
상당히 정직하게 구현. peek하거나 pop할 때 첫 번째 element만 남기고 나머지를 다 pop해버린다.
그리고 나서 pop하느라 순서가 거꾸로 된 spare stack에서 다시 pop하여 원래 순서로 되돌려놓는다.
정직하고 무식한 구현법
"""


# Solution 2
class MyQueue:

    def __init__(self):
        self.input, self.output = [], []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not (self.input or self.output)


"""
위와 비슷하지만 훨씬 똑똑한 구현법. 순서가 바뀌어버린 spare를 그대로 queue의 peek이나 pop에 사용.
output이 비어있다면 다시 input에 있는 걸로 채워준다.
"""