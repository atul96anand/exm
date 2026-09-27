s = "madaaam"

s_list:list =list(s)

n:int = len(s_list)
plnd = True
left=0
right = n -1

while right>left:
    if s_list[left]!= s_list[right]:
        plnd = False
        break
        

    s_list[left],s_list[right] = s_list[right],s_list[left]
    left  += 1
    right -= 1 

if not plnd:
    print(f"the {s} is not a palindrome")
else:
    print(f"{s} is pallindrom")





