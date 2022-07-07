"""
Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание, умножение, деление и возведение в степень.
Программа должна выдавать сообщения об ошибке и продолжать работу при вводе некорректных данных, делении на ноль и возведении нуля в отрицательную степень.
"""


def result(a, b, o):
    if o == "+":
        return print(a + b)
    elif o == "-":
        return print(a - b)
    elif o == "*":
        return print(a * b)
    elif o == "/":
        return print(a / b)
    elif o == "**":
        return print(a ** b)


def main():
    while True:
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            o = input("Введите оператор (+)(-)(*)(/)(**): ")
            result(a, b, o)
        except (ValueError, ArithmeticError, NotImplementedError):
            print("Error 404")


if __name__ == "__main__":
    main()