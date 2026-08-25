from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set(wordList)
        n = len(s)
        if endWord not in s:
            return 0
        q = deque()
        q.append(beginWord)
        vis = dict()
        vis[beginWord] = True
        cnt = 1
        while q:
            m = len(q)
            cnt += 1
            for i in range(m):
                w = q.popleft()
                for j in range(len(w)):
                    for k in range(ord('a'),ord('z')+1):
                        if w[j] != chr(k):
                            nextword = w[:j]+chr(k)+w[j+1:]
                            if nextword == endWord:
                                return cnt
                            if nextword in s and not vis.get(nextword,False):
                                q.append(nextword)
                                vis[nextword] = True
        return 0
