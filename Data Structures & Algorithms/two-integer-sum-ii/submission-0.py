class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i<j:
            if target == numbers[i]+numbers[j] and numbers[i] != numbers[j]:
                break
            if target>numbers[i]+numbers[j]:
                i += 1
            else:
                j -= 1
        return [i+1,j+1]
        