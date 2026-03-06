import json
lib = 'library.json'
def load_library():
    try:
        with open(lib,'r',encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save(data):
    with open(lib,'w',encoding='utf-8') as file:
        json.dump(data,file,ensure_ascii= False,indent=4)
    
def show_books(books):
    print('Список книг')
    for b in books:
        print(f'{b['id']}: {b['title']}: ({b['author']},{b['year']}) | Доступность: {'True' if b['available'] else 'False'}')

def find_book(books):
    term = input("Введите название или автора для поиска: ").strip().lower()
    results = [b for b in books if term in b['title'].lower() or term in b['author'].lower()]
    if results:
        print("Найдено:")
        for r in results:
            print(f"{r['id']}: {r['title']} ({r['author']}, {r['year']}) | Доступность: {'True' if r['available'] else 'False'}")
    else:
        print("Книг не найдено.")

def update_book(books):
    id_ = int(input('Введите ID книги для обновления её состояния: '))
    book = next((b for b in books if b['id'] == id_),None)
    if book:
        book['available'] = not book['available']
        save(books)
        print(f"Состояние книги обновлено!Теперь доступна: {'True' if book['available'] else 'False'}\\n")
    else:
        print("Ошибка: книга с указанным ID не найдена.")

def remove_book(books):
    id_ = int(input("Введите ID книги для удаления: "))
    removed = False
    for i, b in enumerate(books):
        if b['id'] == id_:
            del books[i]
            removed = True
            break
    if removed:
        save(books)
        print("Книга успешно удалена.")
    else:
        print("Ошибка: книга с указанным ID не найдена.")

def menu():
    books = load_library()
    while True:
        print("Меню библиотеки---------------")
        print("1. Показать все книги")
        print("2. Найти книгу")
        print("3. Обновить состояние книги")
        print("4. Удалить книгу")
        print("0. Выход")
        action = input("Ваш выбор: ")
        if action == '0': break
        elif action == '1': show_books(books)
        elif action == '2': find_book(books)
        elif action == '3': update_book(books)
        elif action == '4': remove_book(books)
        else: print("Неправильный ввод. Повторите попытку.")

menu()
