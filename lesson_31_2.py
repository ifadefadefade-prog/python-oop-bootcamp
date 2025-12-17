class ExeptionPrint(Exception):
    pass


class ExeptionPrintSendData(ExeptionPrint):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка: {self.message}"


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f'печать: {str(data)}')

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExeptionPrintSendData('принтер не отвечает')

    def send_to_print(self, data):
        return False


data = PrintData()
data.print('123')
try:
    data.print('123')
except ExeptionPrintSendData:
    print('Не отвечает')
except ExeptionPrint:
    print('Общая ошибка печати')
