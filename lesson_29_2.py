def get_valies():
    try:
        with open('myfile.txt') as f:
            f.write('Hello')
    except BaseException as e:
        print(e)
    else:
        print('Без ошибок')
    finally:
        if f:
            f.close()
            print('Файл закрыт')
