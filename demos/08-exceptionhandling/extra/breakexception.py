class BreakLoopError(Exception):
    pass


def test():
    a = [
        11,
        22,
        33,
        44,
        55,
        66,
    ]
    b = [
        111,
        222,
        333,
        444,
        555,
        666,
    ]
    try:
        for x in a:
            print(f"outer -- x: {x}")
            for y in b:
                if x > 22 and y > 444:
                    raise BreakLoopError("leaving inner loop")
                print(f"inner -- y: {y}")
            print("outer -- after")
            print("-" * 40)
    except BreakLoopError as exp:
        print(f"out of loop -- exp: {exp}")


test()
