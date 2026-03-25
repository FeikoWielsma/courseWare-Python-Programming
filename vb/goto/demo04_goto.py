# Example 4: Using comefrom to let the cleanup code take control itself.
from goto import comefrom, label
def bigFunction2():
    setUp()
    if not doFirstTask():
        label .failed
    if not doSecondTask():
        label .failed
    if not doThirdTask():
        label .failed
    if not doFourthTask():
        label .failed

    comefrom .failed
    cleanUp()

bigFunction2()
print "bigFunction2 done\n"