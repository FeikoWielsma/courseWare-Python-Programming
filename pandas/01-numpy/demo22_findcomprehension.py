import numpy as np

lst = ["aaa","aazzz","zzz", "abder", "rehfwdd" , "dgfhfhfg"", dgthtyjty"]
n = np.array(lst)
result = [i for i,item in enumerate(n) if "hf" in item]
print(result)

for i in result :
    print(lst[i])

