# Реализовать телефонный справочник

# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

# Открыть файл

def open_book():
    telephone_book = []
    book = {}
    with open('text.txt') as data:
        count = 0
        for item in data.readlines():
            key,val = item.strip().split(':')
            book[key] = val
            count += 1
            if count == 3:
                book1 = {}
                book1 = book.copy()
                telephone_book.append(book1)
                book.clear()
                count = 0
    return telephone_book

# Сохранить файл

def save_book(telephone_book):
    with open('text.txt','w') as data:
        for contact in telephone_book:
            for key,val in contact.items():
                data.write(f'{key}:{val}\n')

# Показать контакты

def print_book():
    telephone_book = open_book()
    if telephone_book == []:
        print()
        print('Телефонная книга пуста!')
    else:
        for item in telephone_book:
            for keys in item:
                print(item[keys])
            print()

# Добавить контакт

def add_contact():
    telephone_book = open_book()
    surname = str.title(input('Введите фамилию контакта: '))
    name = str.title(input('Введите имя контакта: '))
    number = input('Введите номер телефона контакта: ')
    contact = {'Surname':surname, 'Name':name, 'Number':number}
    if contact in telephone_book:
        print('Данный контакт существует')
    else:
        telephone_book.append(contact)
    save_book(telephone_book)

# Найти контакт

def search_contact():
    telephone_book = open_book()
    search = str.title(input('Введите фамилию или имя контакта: '))
    count = 0
    for item in telephone_book:
        for keys in item:
            if item[keys] == search:
                count += 1
                print()
                for keys in item:
                    print(item[keys])
                return item
    if count == 0:
        print()
        print('Данный контакт отсутствует!')
            
            
# Изменить контакт

def edit_contact():
    telephone_book = open_book()
    search_item = search_contact()
    for item in telephone_book:
        if search_item == item:
            item['Surname'] = str.title(input('Введите новую фамилию контакта: '))
            item['Name'] = str.title(input('Введите новое имя контакта: '))
            item['Number'] = input('Введите новый номер телефона контакта: ')
    save_book(telephone_book)
    
# Удалить контакт

def delete_contact():
    telephone_book = open_book()
    search_item = search_contact()
    for item in telephone_book:
        if item == search_item:
            telephone_book.remove(item)
    save_book(telephone_book)

def main():
    open('text.txt','a')
    count = -1
    while count != 0:
        print()
        print('Выберите пункт действий:')
        print('1. Показать контакты')
        print('2. Добавить контакт')
        print('3. Найти контакт')
        print('4. Изменить контакт')
        print('5. Удалить контакт')
        print('6. Выход')
        print()
        number = int(input('Введите пункт действия: '))
        if number == 1:
            print()
            print_book()
        elif number == 2:
            print()
            add_contact()
        elif number == 3:
            print()
            search_contact()
        elif number == 4:
            print()
            edit_contact()
        elif number == 5:
            print()
            delete_contact()
        else:
            count = 0
            print()
            print('До скорой встречи!')
if __name__ == '__main__':
    main()