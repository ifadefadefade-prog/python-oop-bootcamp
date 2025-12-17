fp = None
try:
    with open('myfile.txt') as f:
        print(f.read())
except Exception as e:
    print(e)
