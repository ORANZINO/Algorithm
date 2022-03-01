import heapq


def solution(operations):
    max_heap, min_heap = [], []

    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == "I":
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
        elif num == 1:
            if max_heap:
                temp = -heapq.heappop(max_heap)
                min_heap.remove(temp)
        else:
            if min_heap:
                temp = heapq.heappop(min_heap)
                max_heap.remove(-temp)
    return [0, 0] if not max_heap else [-heapq.heappop(max_heap), heapq.heappop(min_heap)]


'''
최대 힙과 최소 힙 2개를 운용하여 답을 도출한다.
'''