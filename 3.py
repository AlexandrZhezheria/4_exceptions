"""
Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год поступления на работу.
Конструктор должен генерировать исключение, если заданы неправильные данные.
Введите список работников с клавиатуры. Выведите всех сотрудников, которые были приняты после заданного года.
"""


class Sotrudnik:
    def __init__(self, name, surname, department, year):
        self.name = name
        self.surname = surname
        self.department = department
        self.year = year

    def __str__(self):
        return f"Сотрудник> {self.name} - Фамилия> {self.surname} - Отдел> {self.department} - Год поступления> {self.year}"


list_of_workers = []


def main():
    while True:
        try:
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            department = int(input("Введите отдел: "))
            year = int(input("Введите год поступления на работу: "))
        except ValueError:
            print("Error 404")
        else:
            sotrudnik = Sotrudnik(name, surname, department, year)
            print(sotrudnik)
            list_of_workers.append(sotrudnik)

        n = int(input(
            "[1] - Посмотреть список струдников \n[2] - Посмотреть сотрудника нужного года \n[3] - Выйти из програмы \n>"))
        if n == 1:
            print(list_of_workers)
        elif n == 2:
            check = int(input("Введите год сотрудника, которого нужно посмотреть: "))
            if sotrudnik in list_of_workers:
                if sotrudnik.year >= check:
                    print(sotrudnik)
                else:
                    print("Не верный год")
                    return False
        else:
            return False


if __name__ == "__main__":
    main()
