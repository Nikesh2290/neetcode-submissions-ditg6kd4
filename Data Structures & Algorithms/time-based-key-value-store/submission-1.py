class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        arr = self.dic.get(key,[])
        arr.append((timestamp,value))
        self.dic[key] = arr

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dic.get(key,[])
        n = len(arr)
        if n==0:
            return ""
        l = 0
        r = n-1
        indx=0
        while l<=r:
            mid = (l+r)//2
            if timestamp == arr[mid][0]:
                return arr[mid][1]
            if timestamp>arr[mid][0]:
                indx = max(indx,mid)
                l = mid+1
            else:
                r = mid-1
        if arr[indx][0] > timestamp:
            return ""
        return arr[indx][1]
            


        
