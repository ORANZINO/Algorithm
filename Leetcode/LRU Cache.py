class CacheItem:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.dic = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        elif key != self.head.key:
            cur = self.dic[key]
            if key == self.tail.key:
                self.tail = self.tail.prev
            if cur.prev is not None:
                cur.prev.next = cur.next
            if cur.next is not None:
                cur.next.prev = cur.prev
            cur.next, cur.prev = self.head, None
            self.head.prev = cur
            self.head = cur
        return self.dic[key].val

    def put(self, key: int, value: int) -> None:
        new = CacheItem(key, value)
        if self.get(key) == -1:
            if self.head is None:
                self.head = new
                self.tail = new
            else:
                new.next, self.head.prev = self.head, new
                self.head = new
            self.dic[key] = new
            if len(self.dic) > self.capacity:
                del self.dic[self.tail.key]
                self.tail = self.tail.prev
                self.tail.next = None
        else:
            self.dic[key].val = value


