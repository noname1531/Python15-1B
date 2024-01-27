#Функции python
"""Функции в python престовляют собой особый участок кода кот который можно вызвать обратившись к нему по имени
которым он был назван. Функции можно можно создать при помоши операции Python - def"""
# def hello():
#     print("Hello world")
# hello()#вызов функции по имени hello

# def it_geeks():
#     print("Geeks - айти курсы в Оше")
#     print(10 + 40)
# it_geeks()

# def add():
#     num1 = int(input("Первое число: "))
#     num2 = int(input("Второе число: "))
#     print(num1 + num2)
# add()

# def mult(num1, num2):
#     print(num1 + num2)
# mult(10, 40)

# def welcome(names:list) -> str: 
#     for name in names:
#         print(f"Здраствуйте {name[0]}.")
# list_names = ['Kurmanbek', 'Beksultan', 'Islam']
# welcome(list_names)

# def chet_nechet(number:int=2) -> str:
#     if number % 2 == 0:
#         print(number, "четный")
#     else:
#         print(number, "нечетное")
# chet_nechet( 45)

# def izogramma(world:str="Geeeks") -> bool:
#     # print(world)
#     if len(set(world.lower())) == len(world.lower()):
#         print(True)
#     else:
#         print(False)
# izogramma("Telegram")
# izogramma("it")
# izogramma("TelEgram")

# def it_geeks():
#     return "Geeks Osh IT"
# it_geeks()

# import time

# def chet_time():
#     start_time = time.time()
#     print("Hello world")
#     time.sleep(1)
#     print("Geeks")
#     end_time = time.time()
#     print(end_time - start_time)
# chet_time()
    
import random

def generate_password():
    letters = "qwertyuiopasdfghjklzxcvbnm"
    # random_letters = random.choice(letters)
    # print(random_letters)
    result = ""
    for i in range(10):
        random_letters = random.choice(letters)
        # print(random_letters)
        result += random_letters
    print(result)

generate_password()