class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mapp = {}
        n = len(position)
        for i in range(n):
            time = (target-position[i])/speed[i]
            val = mapp.get(position[i],0)
            if val == 0:
                mapp[position[i]] = time
            else:
                mapp[position[i]] = max(mapp[position[i]],time)
        temp = sorted(position,reverse=True)
        print(temp)
        print(mapp)
        ans=1
        t = mapp[temp[0]]
        for i in range(1,n):
            if mapp[temp[i]] > t:
                ans += 1
                t = mapp[temp[i]]
        return ans



