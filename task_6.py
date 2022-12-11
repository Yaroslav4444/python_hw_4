"""
6) Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите
внимание, что создаваемый цикл не должен быть бесконечным. Необходимо
предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при
котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle

"""part a"""

list_of_integers = []
"""generating numbers using count()"""

first = int(input("Введите начальное число: "))
last = int(input("Введите конечное число: "))

for el in count(first):
    if el > last:
        break
    print(el)
    list_of_integers.append(el)

"""part b"""

print(list_of_integers)
"""repeating numbers using cycle()"""

count = 0
for item in cycle(list_of_integers):
    if count == len(list_of_integers):
        break
    print(item)
    count += 1
