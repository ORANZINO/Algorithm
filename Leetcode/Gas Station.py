from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = fuel = 0
        for i in range(len(gas)):
            if fuel + gas[i] >= cost[i]:
                fuel += gas[i] - cost[i]
            else:
                start = i + 1
                fuel = 0
        return start

