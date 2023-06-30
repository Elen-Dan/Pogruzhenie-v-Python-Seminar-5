'''
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла. 
'''

import os

full_path = __file__ 
# C:/Users/Joni Dog/Desktop/Home_work-5/job/task_1.py

def info_file(full_path):
    path_file = os.getcwd()
    full_name = full_path.split("/")[-1].split(".")
    name_file, expansion_file = full_name[0], "." + full_name[1]
    info = (path_file, name_file, expansion_file)
    return info

print(info_file(full_path))