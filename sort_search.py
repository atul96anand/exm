class Sort:
    def __init__(self,arr:list[int])->None:
        self.arr = arr
        self.size = len(arr)

    def mrg(self,arr1:list,arr2:list):
        merged:list = []

        i = 0

        j =0

        while i<len(arr1) and j<len(arr2):
            if arr1[i] <arr2[j]:
                merged.append(arr1[i])
                i += 1

            else:
                merged.append(arr2[j])
                j += 1

        if i< len(arr1):
            merged.extend(arr1[i:])
        if j< len(arr2):
            merged.extend(arr2[j:]) 

        return merged

    def merge(self,arr:list):
        if len(arr)>=1:
            return arr
        mid = len(arr)//2

        left = self.merge(arr[:mid])
        right = self.merge(arr[mid:])

        return self.mrg(left,right)

    def bin(self,target,arr):
        left = 0
        right = len(arr) - 1

        mid = (left+right)//2

        while left<=right:
            if arr[mid] == target:
                return mid
            elif target>arr[mid]:
                left = mid+1

            else:
                right = mid-1

        return -1

s = Sort([8,9,1,5,6,2])
print(s.merge(s.arr))






        
