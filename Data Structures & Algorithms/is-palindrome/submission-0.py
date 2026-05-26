class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i=0
        j=n-1
        while i<j:
            if s[i]>='a' and s[i]<='z' or s[i]>='A' and s[i]<='Z':
                while j>i:
                    if s[j]>='a' and s[j]<='z' or s[j]>='A' and s[j]<='Z':
                        if s[i].lower() == s[j].lower():
                            i+=1
                            j-=1
                            break
                        else:
                            return False
                    elif s[i]>='0' and s[i]<='9':
                        return False
                    else:
                        j-=1
            elif s[i]>='0' and s[i]<='9':
                while j>i:
                    if s[j]>='a' and s[j]<='z' or s[j]>='A' and s[j]<='Z':
                        return False
                    elif s[i]>='0' and s[i]<='9':
                        if s[i] == s[j]:
                            i+=1
                            j-=1
                            break
                        else:
                             return False
                    else:
                        j-=1
            else:
                i+=1
        return True