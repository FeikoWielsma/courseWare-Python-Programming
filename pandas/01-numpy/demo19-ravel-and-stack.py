import numpy as np

x= np.array([(1,2,3),(3,4,5)])
print(x.ravel())   # [1 2 3 3 4 5]

x= np.array([(1,2,3),(3,4,5)])
y= np.array([(1,2,3),(3,4,5)])

print(np.vstack((x,y)))
# [[1 2 3]
#  [3 4 5]
#  [1 2 3]
#  [3 4 5]]

print(np.hstack((x,y)))
# [[1 2 3 1 2 3]
#  [3 4 5 3 4 5]]