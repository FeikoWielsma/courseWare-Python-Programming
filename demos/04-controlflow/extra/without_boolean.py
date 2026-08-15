# In Python 3 input() always returns a string, so it is converted before
# it is compared with a number.
number = int(input('Enter a number between 1 and 10: '))
if number <= 10:
    if number >= 1:
        print('Great!')
    else:
        print('Wrong!')
else:
    print('Wrong!')
