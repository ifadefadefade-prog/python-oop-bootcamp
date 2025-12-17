try:
    x, y = map(int, input().split())
    try:
        res = x / y
    except BaseException as e:
        print(e)
except BaseException as e:
    print(e)
finally:
    print('До оператора return')
