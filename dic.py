dic ={
    "p" : 1,
    "r" : 2,
    "o" : 1,
    "g" : 2,
    "a" : 1,
    "m" : 2,
    "i" : 1,
    "n" : 1
}

for char,freq in dic.items():
    

    if freq == 1:
            
            for i in range(len(char)):
                print(char[0])