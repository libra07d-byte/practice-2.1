import csv
def read_txt(filename):
    with open(filename,'r', newline = '',encoding = 'utf-8') as file:
        reader = csv.reader(file)
        next(file)
        data = list(reader)
    return data
def add_product(filename,product_name,price,quantity):
    with open(filename,'a', newline ='',encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([product_name,price,quantity])
def search_product(filenname, product_name):
    data = read_txt(filenname)
    for row in data:
        if row[0].lower() == product_name.lower():
            return row
    return None
def total_cost(filename):
    data = read_txt(filename)
    total = 0
    for row in data:
        price = float(row[1])
        quantity = int(row[2])
        total += price * quantity
    return total
def  save_data(filename,data):
    with open(filename, 'w',newline = '',encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Название,Цена,Количество'])
        writer.writerows(data)
def main():
    filename = 'products.csv'
    data = read_txt(filename)

    while True:
        print('Меню:')
        print('1. Добавить новый товар.')
        print('2. Поиск товара по названию.')
        print('3. Расчет общей стоимости всех товаров на складе.')
        print('4. Выход.')

        choice = input('Выберите действие(1-4): ')
        if choice == '1':
            try:
                product_name = input('Введите название товара: ')
                price = float(input('Введите цену товара: '))
                quantity = int(input('Введите количество товара: ')) 
                add_product(filename,product_name,price,quantity)
                print('Товар добавлен.')
            except ValueError:
                print("ERROR: введено некорректное значение.")
        if choice == '2':
            product_name = input('Введите название товара для поиска: ')
            result = search_product(filename,product_name)
            if result:
                print(f'Название:{result[0]},Цена:{result[1]},Количество:{result[2]}.')
            else:
                print('Товар не найден') 
        if choice == '3':
            total = total_cost(filename)
            print(f'Общая стоимость всех товаров на складе:{total}')
        if choice == '4':
            print('Выход...')
            break
        else:
            print('Неверный выбор.Попробуйте снова.')


main()
