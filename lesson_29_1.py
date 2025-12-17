try:
    x, y = map(int, input().split())
    res = x / y
except BaseException as e:
    print(e)
