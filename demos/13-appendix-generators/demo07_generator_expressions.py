li = [1,2,3,4]

# generator expression, watch the parenthesis
ge = (2*x for x in li)
print (ge)       # <generator object <genexpr> at 0x0085B4E0>
print (next(ge)) # prints 2

for i in ge:      # prints 4, 6 and 8
    print (i)

# list comprehension, watch the block brackets 
lc = [2*x for x in li]
print (lc)  # [2, 4, 6, 8]