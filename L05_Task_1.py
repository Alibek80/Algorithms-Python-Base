# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

from collections import namedtuple

ent_num = int(input("Введите количество предприятий: "))

new_enterprise = namedtuple('new_enterprise', 'name q1 q2 q3 q4 year')

ents = []

for i in range(ent_num):
    name1 = input("Введите наименование предприятия: ")
    q1 = int(input("Введите прибыль за 1 квартал: "))
    q2 = int(input("Введите прибыль за 2 квартал: "))
    q3 = int(input("Введите прибыль за 3 квартал: "))
    q4 = int(input("Введите прибыль за 4 квартал: "))
    year1 = q1 + q2 + q3 + q4
    ents.append(new_enterprise(name1, q1, q2, q3, q4, year1))

avg_profit = sum(ent.year for ent in ents) / ent_num

print("Средняя приьбыль составляет: ", avg_profit)

print("Предприятия, чья прибыль выше среднего: ")

for ent in ents:
    if ent.year > avg_profit:
        print(ent.name)

print("Предприятия, чья прибыль ниже среднего: ")

for ent in ents:
    if ent.year < avg_profit:
        print(ent.name)
