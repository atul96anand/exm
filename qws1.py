arr:list =[4,2,4,3,2,5,3,1]

new_arr =[]

for num in arr:
    if num not in new_arr:
        new_arr.append(num)

print(f"the new arr is {new_arr}")
        
    