import collections


# Solution 1
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ""))
        return s


"""
charset에서 작은 순서대로 가장 앞에 있는 인덱스를 찾는다.
그 이후를 suffix라고 하고, set(s)가 set(suffix)와 같다면, 그 이전 것은 무시해도 된다. 
왜냐하면 뒤에 있는 것들이 사용될 것이기 때문이다.
다만, 그렇지 않다면 무시해선 안된다. suffix에 안 나온 char가 있고, 이를 포함해야 하기 때문이다.
이런 논리로 recursion을 진행하는 방법
"""


# Solution 2
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Counter(s), []

        for char in s:
            counter[char] -= 1
            if char in stack:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)
        return ''.join(stack)


"""
stack으로 하나하나 쌓아가며 더 작은 char가 나오고 뒤에 같은 char가 나오면 pop하는 방식(뒤에 거 쓸거니까)
stack이 쌓이는것이 pop돼야할 우선순위대로 쌓이기 때문에 가능한 방식.
"""