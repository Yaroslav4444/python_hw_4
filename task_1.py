"""
1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, user_surname, user_hours, user_rate = argv
print(argv)


def payroll_calculation(hours, rate):
    """calculation of employee's salary"""

    print(
        f"За месяц сотрудник {user_surname} заработал : {hours * rate} "
        f"+ 5000 премия")


payroll_calculation(int(user_hours), int(user_rate))
