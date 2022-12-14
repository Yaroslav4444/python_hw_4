"""
2) Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для
формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
list_of_numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

sorted_list_of_numbers = [list_of_numbers[el] for el in
                          range(1, len(list_of_numbers))
                          if list_of_numbers[el] > list_of_numbers[el - 1]]
"""search for items that are larger than the previous one"""

print(sorted_list_of_numbers)
