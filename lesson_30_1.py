def func2():
    try:
        return 1 / 0
    except BaseException as e:
        print(e)


def func1():
    try:
        return func2
    except BaseException as e:
        print(e)


func1()
