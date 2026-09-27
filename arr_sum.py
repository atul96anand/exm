def arr_sum(arr:list, index:int):
    if index == len(arr)-1:
        return arr[index]

    return arr[index] + arr_sum(arr,index+1)

print(f" the total sum is --> {arr_sum([2,5,3,7,6],0)}")
