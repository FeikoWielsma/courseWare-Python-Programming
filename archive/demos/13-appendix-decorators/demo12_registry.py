registry = {}


def register(cls):
    registry[cls.__clsid__] = cls
    return cls


@register
class Foo(object):
    __clsid__ = "123-456"


@register
class Bar(object):
    __clsid__ = "ABC-EFG"


print(registry)
