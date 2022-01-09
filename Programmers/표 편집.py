class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def solution(n, k, cmd):
    deleted = []
    head = temp = ListNode(0)
    now = None
    if k == 0:
        now = head
    for i in range(1, n):
        temp.next = ListNode(i, prev=temp)
        temp = temp.next
        if i == k:
            now = temp
    for c in cmd:
        if c[0] == 'D':
            num = int(c.split()[1])
            for _ in range(num):
                now = now.next
        elif c[0] == 'U':
            num = int(c.split()[1])
            for _ in range(num):
                now = now.prev
        elif c[0] == 'C':
            if now.prev:
                now.prev.next = now.next
            if now.next:
                now.next.prev = now.prev
            deleted.append(now)
            if not now.next:
                now = now.prev
            else:
                now = now.next
        elif c[0] == 'Z':
            temp = deleted.pop()
            if temp.next:
                temp.next.prev = temp
            if temp.prev:
                temp.prev.next = temp

    answer = ['O'] * n
    for d in deleted:
        answer[d.val] = 'X'

    return ''.join(answer)


"""
삭제 및 복원이 용이하도록 linked list 형식으로 구현하였다.
"""