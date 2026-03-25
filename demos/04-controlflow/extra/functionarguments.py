def fancy(obj):
    print 'fancy fancy -- %s -- fancy fancy' % (obj, )
    
def plain(obj):
    print 'plain -- %s -- plain' % (obj, )
    
def show(func, obj):
    func(obj)
    
def main():
    a = {'aa': 11, 'bb': 22, }
    show(fancy, a)
    show(plain, a)
    
if __name__ == '__main__':
    main()
