"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
#1 сложность O(NLog N)
maximum = [10, 200, 400, 20, 100, 1000, 1002]
print(sorted(maximum, reverse=True)[:3])



#2 сложность O(N^2)
def maximum_n(max_n):
    swap = True
    while swap:
        swap = False
        for i in range(len(max_n) - 1):
            if max_n[i] < max_n[i + 1]:
                max_n[i], max_n[i + 1] = max_n[i + 1], max_n[i]
                swap = True


list_of_max = [100, 500, 4444, 111, 2224]
maximum_n(list_of_max)
print(list_of_max[0:3])


# Первый вариант конечно же проще, и быстрее ...