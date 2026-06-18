from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        st = deque()

        for i in range(n):
            if tokens[i] in {'+','-','*','/'}:
                first = st.pop()
                second = st.pop()
                val=0
                if tokens[i] == '+':
                    val = second+first
                elif tokens[i] == '-':
                    val = second-first
                elif tokens[i] == '*':
                    val = second*first
                else:
                    val = int(second/first)
                st.append(val)
            else:
                st.append(int(tokens[i]))
        ans = st.pop()
        return ans



