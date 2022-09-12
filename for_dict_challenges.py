from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
count_list=[]
for dic_student in students:
    count_list.append(dic_student["first_name"])
count_dic=Counter(count_list)
for name, count in count_dic.items():
    print(f"{name}: {count}")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
count_list=[]
for dic_student in students:
    count_list.append(dic_student["first_name"])
count_dic=Counter(count_list)
print(f'Самое частое имя среди учеников: {Counter(count_list).most_common(1)[0][0]}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for j,s_class in enumerate(school_students,start=1):
    count_list=[]
    for dic_student in s_class:
        count_list.append(dic_student["first_name"])
    count_dic=Counter(count_list)
    print(f'Самое частое имя среди учеников {j} класса: {count_dic.most_common(1)[0][0]}')
    


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for school_class in school:           
    name_list = [student['first_name'] for student in school_class['students']]
    count_girls,count_boys=0,0
    for name in name_list:
        if is_male[name]:
            count_boys+=1
        else:
            count_girls+=1      
    print(f"Класс {school_class['class']}: девочки {count_girls}, мальчики {count_boys}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

''
count_list=[]
list_class=[]
for class_s in school:
    list_class.append(class_s['students'])
    class_g=0
    class_b=0
    for students in list_class:
        for names in students:
            name=names['first_name']
            if is_male[name]:
                class_b+=1
            else:
                class_g+=1
        count_list.append({"class":class_s['class'],"boys": class_b, 'girls': class_g})

girls_max =max ([g_count['girls'] for g_count in count_list])
boys_max= max([b_count['boys'] for b_count in count_list])

class_girls_max = [g_count['class'] for g_count in count_list if g_count['girls'] ==  girls_max][0]
class_boys_max = [b_count['class'] for b_count in count_list if b_count['boys'] == boys_max][0]

print(f'Больше всего мальчиков в классе {class_boys_max}')
print(f'Больше всего девочек в классе {class_girls_max}') 