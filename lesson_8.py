# #Молули python 
# def hello_world():
#     return 'Hello, world!'
# def add(num1:int=1, num2:int=1) -> int:
#     return num1 + num2
# def it_courses(language:str) -> str:
#     return f'Programming Languages {language}'

# it="Geeks"

# def chet_nechet(numbers:[tuple, list]) -> str:
#     for num in numbers:
#         if num % 2 == 0 :
#             print(num, "ch")
#         else:
#             print(num, 'ne')

# def welcome_name(names:list) ->  str:
#     for name in names:
#         print("Hello", name)


# # работа с файлами в Python:
# f = open('hello.txt', 'w')
# f.write('Hello world and Geeks')
# f.close()

# r = open('hello.txt', 'r')
# print(r.read())
# r.close()

# python_file =open('file_test.py', 'w')
# python_file.write('print("Hello world")')
# python_file.close()

# read_python_file = open('lesson_8.py', 'r')
# print(read_python_file.read())
# read_python_file.close()

test = open('file_test.py', 'w')
test.write('print("Hello Geeks")')
test.close()

encode =open('test,txt', 'w', encoding='utf-8')
encode.write('Привет всем и привет Geeks')
decode = open('test,txt', 'r')


read_encode = open('test.txt', 'r', encoding='utf-8')
print(read_encode.read())
read_encode.close()


with open('close.txt', "w", encoding='utf-8')as close:
    close.write('с помощью with можно не закрывать он сам закроется')
