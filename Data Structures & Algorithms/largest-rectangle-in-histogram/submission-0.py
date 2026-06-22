from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = deque()
        ans=0
        n = len(heights)
        for i in range(n):
            while len(st) > 0 and heights[i]<=heights[st[-1]]:
                        indx = st.pop()
                        prev_indx=-1
                        if len(st) > 0:
                            prev_indx = st[-1]
                        area = (i-prev_indx - 1)*heights[indx]
                        ans = max(ans,area)
            st.append(i)
        while len(st) > 0:
            indx = st.pop()
            prev_indx=-1
            if len(st) > 0:
                prev_indx = st[-1]
            area = (n-prev_indx - 1)*heights[indx]
            ans = max(ans,area)
        return ans
        