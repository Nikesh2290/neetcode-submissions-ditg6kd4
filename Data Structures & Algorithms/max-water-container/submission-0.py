class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i=0
        j=n-1
        max_water=0
        while i<j:
            max_water = max(max_water,(j-i)*min(heights[i],heights[j]))
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_water