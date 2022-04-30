import sys

sys.setrecursionlimit(int(1e6))


class TreeNode:
    def __init__(self, x, y, idx, left=None, right=None, parent=None):
        self.x = x
        self.y = y
        self.idx = idx
        self.left = left
        self.right = right
        self.parent = parent
        self.left_limit = 0
        self.right_limit = int(1e5)


def preorder(node, arr):
    if node is not None:
        arr.append(node.idx)
        preorder(node.left, arr)
        preorder(node.right, arr)
        return arr


def postorder(node, arr):
    if node is not None:
        postorder(node.left, arr)
        postorder(node.right, arr)
        arr.append(node.idx)
        return arr


def solution(nodeinfo):
    nodeinfo = sorted([TreeNode(nodeinfo[i][0], nodeinfo[i][1], i + 1) for i in range(len(nodeinfo))],
                      key=lambda node: (node.y, node.x), reverse=True)

    prev, nxt, prev_idx = 0, 1, 0

    for i in range(1, len(nodeinfo)):
        if nodeinfo[i].y != nodeinfo[nxt].y:
            prev_idx = prev = nxt
            nxt = i
        while not (nodeinfo[prev_idx].left_limit <= nodeinfo[i].x <= nodeinfo[prev_idx].right_limit):
            prev_idx += 1
        nodeinfo[i].parent = nodeinfo[prev_idx]
        if nodeinfo[i].x < nodeinfo[prev_idx].x:
            nodeinfo[prev_idx].left = nodeinfo[i]
            nodeinfo[i].right_limit = nodeinfo[prev_idx].x - 1
            nodeinfo[i].left_limit = nodeinfo[prev_idx].left_limit
        else:
            nodeinfo[prev_idx].right = nodeinfo[i]
            nodeinfo[i].right_limit = nodeinfo[prev_idx].right_limit
            nodeinfo[i].left_limit = nodeinfo[prev_idx].x + 1

    return [preorder(nodeinfo[0], []), postorder(nodeinfo[0], [])]

