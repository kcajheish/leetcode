from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        volume = 0
        start = 0
        total_surplus = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_surplus += diff
            volume += diff
            if volume < 0:
                start = i + 1
                volume = 0
        return start if total_surplus >= 0 else -1

    def canCompleteCircuitBruteForce(self, gas: List[int], cost: List[int]) -> int:
        for start in range(len(gas)):
            volume = 0
            for i in range(0, len(gas)):
                pos = (start + i) % len(gas)
                volume += gas[pos] - cost[pos]
                if volume < 0:
                    break
            if volume >= 0:
                return start
        return -1
