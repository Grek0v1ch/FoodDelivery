import os


class System:
    @staticmethod
    def validate_integer_in_range(a: int, b: int) -> int:
        while True:
            value = input(f'Введите целое число в диапазоне от {a} до {b}: ')
            try:
                int_value = int(value)
                if a <= int_value <= b:
                    return int_value
                else:
                    print('Введенное значение не входит в диапазон.'
                          ' Повторите ввод')
            except ValueError:
                print('Введенное значение не является целым числом.'
                      ' Повторите ввод')
                pass

    @staticmethod
    def clear_terminal():
        if os.name == 'posix':  # для MacOS и Linux
            _ = os.system('clear')
        else:  # для Windows
            _ = os.system('cls')