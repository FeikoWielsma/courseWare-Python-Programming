def add_to_dict(name, value, dic=None):
    if dic is None:
        dic = {}
    dic[name] = value
    return dic


def test():
    dic1 = {'albert': 'cute'}
    print(add_to_dict('barry', 'funny', dic1))
    print(add_to_dict('charlene', 'smart', dic1))
    print(add_to_dict('darryl', 'outrageous'))
    print(add_to_dict('eddie', 'friendly'))


test()
