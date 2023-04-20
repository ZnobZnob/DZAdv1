from datetime import datetime, date, time
import dice
from application.salary import calculate_salary
from application.db.people import get_employees


def main():
    print(f'Команда 1: calculate_salary\n'
          f'Команда 2: get_employees\n'
          f'Команда 3: Бросить кубик д20\n'
          f'Команда 4: Выход')
    while True:
        command = int(input('Введите команду:'))
        date = datetime.now()
        if command == 1:
            calculate_salary()
            print(f'Date: {date}')
        if command == 2:
            get_employees()
            print(f'Date: {date}')
        if command == 3:
            dice20 = dice.roll('1d20')
            print(f'D20: {dice20}\nDate: {date}')
        if command == 4:
            print(f'End time: {date}')
            break

if __name__ == '__main__':
    main()





