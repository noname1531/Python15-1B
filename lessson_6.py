# #Исключение try, except
# try: 
#     print(100 / 0)
# except ZeroDivisionError:
#     print("Деление на нроль невозможно")

# try: 
#     Name = "Kurmanbek"
#     print(name1)
# except NameError:
#     print("Обаоботали ошибку")

# while True:
#     try:
#        num1 = int(input("первое число: "))
#        operator = input("+, -, *, /: ")
#        num2 = int(input("Второе число: "))
#        if operator == "+":
#         print(num1 + num2)
#        elif operator == "-":
#         print(num1 - num2)
#        elif operator == "*":
#         print(num1 * num2)
#        elif operator == "/":
#         try: 
#             print(num1 / num2)
#         except ZeroDivisionError:
#             print("Деление на ноль невозможно")
#        else: 
#         print("Токого оператра нету")
#     except ValueError:
#       print("Введите число!")

# raise ValueError("Мы вызволи сами эту ошибку")

#Множество set
# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = [3, 4, 5, 6, 7]
# print(numbers1 + numbers2)
# print(set(numbers1 + numbers2))


# name = {"Islam", "Syimyk", "Timur", "Islam", "Nurbolot", "Timur"}
# print(name)

# st = {True, "Geeks", 10, 30.1, (10, 20, 30)}
# print(st)

# cars = {"BMW", "Lexus", "Mercedes", "Zeekr", "Toyota", "BMW" }
# print(cars)
# cars.add("BMW")
# print(cars)
# cars.add("Tesla")
# print(cars)
# cars.remove("Zeekr")
# print(cars)
# # print(cars[0])
# cars.pop()
# print(cars)

#frozenset
# frozn_set = frozenset({10, 20, 30, 40, 50, 10, 20})
# print(frozn_set)
# print(type(frozn_set))

#Тип даных dictionary - словарь
# student = {'name':'Nurbolot', 'age':19}
# print(student)

# student.setdefault('language', 'Python')
# print(student)

# print(student['name'])
# print(student['language'])

# student.pop('age')
# print(student)

# student['language'] = "JavaScript"
# print(student)

# geeks ={'titel':'Geeks', 'count_student':412, 'count_employees':20}
# print(geeks)
# print(geeks.keys())
# print(geeks.values())