def get_values():
    try:
        x, y = map(int, input().split())
        return x, y
    except BaseException as e:
        print(e)
    finally:
        print('До оператора return')


x, y = get_values()
print(x, y)
