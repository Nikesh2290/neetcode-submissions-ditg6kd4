class Solution:

    def encode(self, strs: List[str]) -> str:
        sep = "."
        s = ""
        if len(strs)>=1:
            s = "1"
            s += sep.join(strs)
        else:
            s = "0"
        return s

    def decode(self, s: str) -> List[str]:
        sep = "."
        strs = []
        l = s[0]
        if l == "1":
            s = s[1:]
            strs = s.split(sep)
        return strs
