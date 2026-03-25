import numpy as np

a = np.array( [20,30,40,50] )
b = np.arange( 4 )

print (b) # [0, 1, 2, 3])

c = a-b
print (c) # [20, 29,38, 47])

b**2 
print (b)            # [0, 1, 4, 9]
print (10*np.sin(a)) # [ 9.12945251, -9.88031624, 7.4511316 , -2.62374854]

A = np.array( [[1,1], [0,1]] )
B = np.array( [[2,0], [3,4]] )
print (A*B) # elementwise product : [2, 0],[0, 4]]
print (A.dot(B)) # matrix product [[5, 4],[3, 4]])