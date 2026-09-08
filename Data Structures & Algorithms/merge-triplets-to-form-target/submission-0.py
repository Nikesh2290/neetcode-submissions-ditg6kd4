class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:  
        x,y,z = False,False,False
        for a,b,c in triplets:
            if a == target[0] and b<=target[1] and c<=target[2]:
                x = True
            if b == target[1] and a<=target[0] and c<=target[2]:
                y = True
            if c == target[2] and b<=target[1] and a<=target[0]:
                z = True
        if x and y and z:
            return True
        return False