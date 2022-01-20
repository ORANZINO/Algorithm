class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 3000
        self.table = [None] * self.size

    def put(self, key: int, value: int) -> None:
        hashed_key = key % self.size
        if self.table[hashed_key] is None:
            self.table[hashed_key] = ListNode(key, value)
        else:
            temp = self.table[hashed_key]
            while temp:
                if temp.key == key:
                    temp.value = value
                    return
                if temp.next is None:
                    break
                temp = temp.next

            temp.next = ListNode(key, value)

    def get(self, key: int) -> int:
        hashed_key = key % self.size
        if self.table[hashed_key] is None:
            return -1
        else:
            temp = self.table[hashed_key]
            while temp is not None and temp.key != key:
                temp = temp.next
            if temp is None:
                return -1
            else:
                return temp.value

    def remove(self, key: int) -> None:
        hashed_key = key % self.size
        if self.table[hashed_key] is not None:
            temp = self.table[hashed_key]
            if temp.key == key:
                self.table[hashed_key] = temp.next
            while temp is not None and temp.next is not None:
                if temp.next.key == key:
                    temp.next = temp.next.next
                    return
                temp = temp.next