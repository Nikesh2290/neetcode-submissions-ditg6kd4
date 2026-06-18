from collections import deque
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        st = deque()
        n = len(temp)
        output = [0]*n
        for i in range(n):
            while len(st)>0 and temp[i]>temp[st[-1]]:
                    output[st[-1]] = i-st[-1]
                    st.pop()
            st.append(i)
        return output


