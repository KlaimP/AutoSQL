
import pyodbc;
import random;

#for driver in pyodbc.drivers():
   # print(driver)
print('Подключение к БД')
command = 'INSERT INTO ';

with open("info.txt", encoding='utf-8') as files:
    info = [row.strip()[row.strip().find("=")+1 : ] for row in files]

connectionString = (r'Driver={SQL Server};Server='+info[0]+';Database='+info[1]+';Trusted_Connection=yes;')
connection = pyodbc.connect(connectionString, autocommit=True)
dbCursor = connection.cursor()
print('Сервер: ' + info[0] + '\nБаза данных: ' + info[1])

print('Подключение к БД успешно\n')

print('Начинают заноситься данные...')

with open("data/nameM.txt", encoding='utf-8') as files:
    name_M = [row.strip() for row in files]

with open("data/patronymicM.txt", encoding='utf-8') as files:
    middle_name_M = [row.strip() for row in files]

with open("data/surnameM.txt", encoding='utf-8') as files:
    family_M = [row.strip() for row in files]

with open("data/date.txt", encoding='utf-8') as files:
    date = [row.strip() for row in files]

with open("data/number.txt", encoding='utf-8') as files:
    number = [row.strip() for row in files]

with open("data/address.txt", encoding='utf-8') as files:
    address = [row.strip() for row in files]

print('Данные успешно занесены\n')

print('Введите название таблицы:')
tabl = input()
print('Введите название столбцов через запятую(Как если бы в запросе):')
stolb = input()

command = command + tabl + '(' + stolb + ') VALUES '
print(command + '\n')

count = stolb.count(',') + 1

mass = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

print('1 - Имена, 2 - Фамилии, 3 - Отчества')
print('4 - Номера телефонов, 5 - Адреса, 6 - Даты')
for i in range(0, count):
    yes = input()
    if yes == '1':
        print('Имя')
        mass[i] = 1
    elif yes == '2':
        print('Фамилия')
        mass[i] = 2
    elif yes == '3':
        print('Отчество')
        mass[i] = 3
    elif yes == '4':
        print('Номер телефона')
        mass[i] = 4
    elif yes == '5':
        print('Адрес')
        mass[i] = 5
    elif yes == '6':
        print('Дата')
        mass[i] = 6

print('Сколько строк занести?')
strok = int(input())

for i in range(0, strok):
    requestString = command + '('
    for j in range(0, count):
            if mass[j] == 1:
                requestString += "'"+name_M[random.randint(0,99)]+"'"
                if j != count-1:
                    requestString += ','
            elif mass[j] == 2:
                requestString += "'"+family_M[random.randint(0,99)]+"'"
                if j != count-1:
                    requestString += ','
            elif mass[j] == 3:
                requestString += "'"+middle_name_M[random.randint(0,99)]+"'"
                if j != count-1:
                    requestString += ','
            elif mass[j] == 4:
                requestString += "'"+number[random.randint(0,999)]+"'"
                if j != count-1:
                    requestString += ','
            elif mass[j] == 5:
                requestString += "'"+address[random.randint(0,999)]+"'"
                if j != count-1:
                    requestString += ','
            elif mass[j] == 6:
                requestString += "'"+date[random.randint(0,999)]+"'"
                if j != count-1:
                    requestString += ','
    requestString += ');'
    print(requestString)
    dbCursor.execute(requestString)
    connection.commit()
