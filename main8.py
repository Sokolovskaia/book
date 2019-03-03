from lib8 import create_book, add_books, list_books, search_books
# TODO: tags - новый ключ в dict'е      подумать можно ли к одному объект несколько одинаковых тегов


# TODO: tags - война, любовь
# TODO: tags - поезд, любовь
# TODO: 1. Как хранить (тип данных)
# TODO: 2. Как искать (полное совпадение?)
# TODO: 3. Написать функция поиска по тегам
# TODO: 4(advanced). искать по тегам #имя тега

books = []

war_and_piece = create_book(
    'Война и мир',
    'Толстой',
    1000,
    True)

anna_karrenina = create_book(
    'Анна Каренина',
    'Толстой',
    500,
    False)

add_books(books, war_and_piece)
add_books(books, anna_karrenina)


# print(len(books))
# print(books)

# print(list_books(books, 1, 1))
# print(list_books(books, 2, 1))


print(search_books(books, 'каре'))
print(search_books(books, 'толстой'))
print(search_books(books, 'стругацкие'))