from typing import List
import collections


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1
                counter.subtract(task)
                if counter[task] == 0:
                    del counter[task]
            if not counter:
                break
            result += n - sub_count + 1
        return result