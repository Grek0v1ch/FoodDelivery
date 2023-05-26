class Validator:
    @staticmethod
    def validate_integer(a: int, b: int) -> int:
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
