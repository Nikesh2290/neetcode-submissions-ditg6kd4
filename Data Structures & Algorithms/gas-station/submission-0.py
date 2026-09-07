class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        si=0
        fuel = 0
        for i in range(2*n):
            fuel += gas[i%n] - cost[i%n]
            if fuel< 0:
                fuel = 0
                si = i+1
            
        if si<n:
            return si
        return -1




