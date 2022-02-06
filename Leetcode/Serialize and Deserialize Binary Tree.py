import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        q = collections.deque([root])
        answer = []
        while q:
            temp = q.popleft()
            if temp:
                q.append(temp.left)
                q.append(temp.right)
                answer.append(str(temp.val))
            else:
                answer.append('#')
        return ' '.join(answer)


    def deserialize(self, data):
        arr = list(data.split())
        if arr[0] == '#':
            return None
        root = TreeNode(int(arr[0]))
        q = collections.deque([root])
        index = 1
        while q:
            temp = q.popleft()
            if arr[index] != '#':
                temp.left = TreeNode(int(arr[index]))
                q.append(temp.left)
            index += 1
            if arr[index] != '#':
                temp.right = TreeNode(int(arr[index]))
                q.append(temp.right)
            index += 1
        return root


"""
BFS를 사용하여 직렬화하고 같은 방식으로 큐를 사용하여 역직렬화한다.
"""