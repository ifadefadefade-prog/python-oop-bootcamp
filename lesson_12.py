class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwds) -> int:
        if not isinstance(args[0], str):
            raise TypeError('Аргумент дожен быть другой')
        return args[0].strip(self.__chars)
    
temp = StripChars("?:/.;! ")
res = temp(' Hello World! ')
print(res)