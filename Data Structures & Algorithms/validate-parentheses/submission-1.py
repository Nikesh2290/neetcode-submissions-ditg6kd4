from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        for char in s:
            if char == '(' or char == '[' or char == '{':
                st.append(char)
            else:
                if len(st) == 0:
                    return False
                top_item = st.pop()
                if (top_item == '(' and char != ')') or (top_item == '{' and char != '}') or (top_item == '[' and char != ']'):
                    return False
        if len(st) == 0:
            return True
        return False