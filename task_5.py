"""
5) Реализовать формирование списка, используя функцию range() и возможности
генератора. В список должны войти четные числа от 100 до 1000
(включая границы). Необходимо получить результат вычисления произведения всех
элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

items = list(range(100, 1001, 2))
print(items)

multiplication_list = reduce(lambda x, y: x * y, items)
"""multiplying list items using reduce()"""

print(multiplication_list)
