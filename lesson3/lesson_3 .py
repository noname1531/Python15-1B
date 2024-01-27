#опирации сравнения
#bool-True, False
#print(10 == 10)
#print(30 == 50)

#print(5 != 5)
#print(100 != 100.1)

#print(9 > 8)
#print(18 > 17)

#print(600 < 599)
#print(0.7456 < 0.7456)

#print(5000 <= 5000)
#print(5215 <= 7515)
#print(6588 <= 5246)

#print(10 >= 10.0)
#print(9.9 >= 9.99)

#Условие if,else,elif
#num1 = 10
#num2 = 20
#if num1 > num2:
    #print("num1 > num2")
#else:
    #print("num2 > num1")

#bob = 75
#if bob % 2 == 0:
    #print(bob,"True")
#else:
    #print(bob,"False")

login = input("Логин: ")
password = input("пороль: ")
if login == "berserk":
    if password == "15312024":
        print("hi")
    else:
        print("lol")
else:
    print("kek")

######################################

login = input("login: ")
password = input("password: ")
if login == "bob" and password == "lol":
    print("true")
else:
    print("false")
#############Google################
google_login = input("gg: ")
if google_login == "bob@gmail.com":
    google_password = input("dd: ")
    if google_password == "5555":
        print("boom")
    else:
        print("kek")
else:
    print("lol")

#Келькулятор
number1 = int(input("number1: "))
operator = input("+,-,*,/: ")
number2 = int(input("number2: "))
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("kek")

