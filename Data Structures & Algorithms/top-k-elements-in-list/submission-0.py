class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for val in nums:
            dic[val] = dic.get(val,0)+1
        sorted_dic = dict(sorted(dic.items(),key= lambda item: item[1], reverse=True))
        print(sorted_dic)
        ans = []
        cnt=k
        for k,v in sorted_dic.items():
            cnt-=1
            ans.append(k)
            if cnt<=0:
                break
        return ans