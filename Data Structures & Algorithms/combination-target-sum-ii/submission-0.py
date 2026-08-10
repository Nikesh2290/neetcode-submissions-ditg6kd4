class Solution:
    def solve(self,c,target,final_list,temp,n,i):
        if target == 0:
            final_list.append(list(temp))            
            return
        if i>=n or target<0:
            return 
        temp.append(c[i])
        self.solve(c,target-c[i],final_list,temp,n,i+1)
        temp.pop()
        while i<n-1 and c[i+1] == c[i]:
            i += 1
        self.solve(c,target,final_list,temp,n,i+1)

            
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c = sorted(candidates)
        n = len(candidates)
        final_list = []
        self.solve(c,target,final_list,[],n,0)
        return final_list