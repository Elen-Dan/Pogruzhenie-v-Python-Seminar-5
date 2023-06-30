'''
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида «10.25%».
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии.
'''

people = ['Иван', 'Петр', 'Сергей']
salary = [25_000, 35_000, 45_000]
rates = ['17%', '23.4%', '33.3%']

def summ_salary_rate(list_name, list_rate, list_award):
    dict_func = {}
    for name_key, rate, award in zip(list_name, list_rate, list_award):
        dict_func[name_key] = rate + ((rate / 100) * (float(award.replace("%",""))))
    return dict_func
    print(dict_func)

print(f'\n{summ_salary_rate(people, salary, rates)}\n')

dict_generator = {name_key: rate + ((rate / 100) * (float(award.replace("%","")))) for name_key, rate, award in zip(people, salary, rates)}
for key, values in dict_generator.items():
    print(f"Имя сотрудника: {key}. \t Зарплата сотрудника с учётом премии: {values}\n")