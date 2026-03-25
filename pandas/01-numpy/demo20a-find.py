# Python Program illustrating
# numpy.char.find() method
import numpy as np

arr = ['vdsdsttetteteAAAa', 'AAAAAAAaattttds', 'AAaaxxxxtt', 'AAaaXDSDdscz']


print ("\nfind of 'Aa'", np.char.find(arr, 'Aa'))
print ("find of 'Aa'", np.char.find(arr, 'Aa', start = 8))
