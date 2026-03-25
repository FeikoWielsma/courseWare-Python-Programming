# Example 3: Cleaning up after something fails:
from goto import goto, label

# Imagine that these are real worker functions.
def setUp(): print "setUp"
def doFirstTask(): print 1; return True
def doSecondTask(): print 2; return True
def doThirdTask(): print 3; return False  # This one pretends to fail.
def doFourthTask(): print 4; return True
def cleanUp(): print "cleanUp"

# This prints "setUp, 1, 2, 3, cleanUp" - no "4" because doThirdTask fails.
def bigFunction1():
    setUp()
    if not doFirstTask():
        goto .cleanup
    if not doSecondTask():
        goto .cleanup
    if not doThirdTask():
        goto .cleanup
    if not doFourthTask():
        goto .cleanup

    label .cleanup
    cleanUp()

bigFunction1()
print "bigFunction1 done\n"