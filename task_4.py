from datetime import datetime
import csv

log = "calculator.log"
local_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def write_log(fields):
    with open(log,'a',encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(fields)

def calculator(x, y, operation):
    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == '*':
        result = x * y
    elif operation == '/':
        if y != 0:
            result = x / y
        else:
            result = 'Ошибка: деление на ноль'
    else:
        result = 'Ошибка: неизвестная операция'
    fields = [f'{local_now} {str(x)} {operation} {str(y)} = {result}']
    write_log(fields)
    return result

def last_operations():
    with open('calculator.log', 'r') as file:
        lines = file.readlines()
        return lines[-5:]

def clear_log():
    with open('calculator.log', 'w') as file:
        file.write('')

while True:
    try:
        x = float(input('Введите первое число: '))
        y = float(input('Введиет второе число: '))
        operation = input('Введите операцию (+, -, *, /): ')
        result = calculator(x,y,operation)
        print(f"Результат операции:{result}")
        last_oper = last_operations()
        print(f'Последние 5 операций: {last_oper}')
        clear = input('Очистить лог-файл?(да/нет):')
        if clear == 'да':
            clear_log()
            print('лог-файл очищен')
        choice = input('Продолжить?(для выхода введите "Выход"):')
        if choice == 'Выход':
            print('Выход...')
            break
    except ValueError:
            print("ERROR: введено некорректное значение.")
