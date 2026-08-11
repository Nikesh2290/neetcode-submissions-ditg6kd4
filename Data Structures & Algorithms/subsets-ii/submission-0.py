class Solution:
    def solve(self,arr,ans,temp,i,n):
        if i >= n:
            ans.append(list(temp))
            return
        temp.append(arr[i])
        self.solve(arr,ans,temp,i+1,n)
        temp.pop()
        while i < n-1 and arr[i+1] == arr[i]:
            i += 1
        self.solve(arr,ans,temp,i+1,n)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        n = len(nums)
        ans = []
        self.solve(arr,ans,[],0,n)
        return ans