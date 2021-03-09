"""
Задание 1
Создайте программу, хранящую информацию о вели-
ких баскетболистах. Нужно хранить ФИО баскетболиста и
его рост. Требуется реализовать возможность добавления,
удаления, поиска, замены данных. Используйте словарь
для хранения информации.
"""

# basketball_players = [
#     {"ФИО": "Майкл Джордан", "Рост": 198},
#     {"ФИО": "Уилт Чемберлен", "Рост": 216},
#     {"ФИО": "Карим Абдул-Джаббар", "Рост": 218}
# ]
#
#
# def add_player_func():
#     player = input("Введите ФИО игрока: ")
#     height = input("Введите рост игрока: ")
#     basketball_players.append({"ФИО": player, "Рост": height})
#
#
# def delete_player_func():
#     player = input("Введите ФИО игрока, которого хотите удалить: ")
#     for i in range(len(basketball_players)-1, 0, -1):
#         if basketball_players[i]["ФИО"] == player:
#             basketball_players.pop(i)
#
#
# def search_players_func():
#     player = input("Введите ФИО игрока, которого хотите найти: ")
#     for i in range(0, len(basketball_players)):
#         if basketball_players[i]["ФИО"] == player:
#             print(basketball_players[i])
#
#
# def edit_player_func():
#     player = input("Введите ФИО игрока, которого хотите изменить: ")
#     for i in range(0, len(basketball_players)):
#         if basketball_players[i]["ФИО"] == player:
#             edit_player = input("Введите ФИО игрока: ")
#             edit_height = input("Введите рост игрока: ")
#             basketball_players[i] = {"ФИО": edit_player, "Рост": edit_height}


# while True:
#     controls = input("Введите действие "
#                      "(добавление - 1, удаление - 2, поиск - 3, замена - 4, показать список - 5, "
#                      "закрыть программу - 0): ")
#     if controls == "1":
#         add_player_func()
#     elif controls == "2":
#         delete_player_func()
#     elif controls == "3":
#         search_players_func()
#     elif controls == "4":
#         edit_player_func()
#     elif controls == "5":
#         print(basketball_players)
#     elif controls == "0":
#         exit(0)
#     else:
#         print("Нет такого действия!")
#         continue

"""
Задание 2
Создайте программу «Англо-французский словарь».
Нужно хранить слово на английском языке и его перевод
на французский. Требуется реализовать возможность до-
бавления, удаления, поиска, замены данных. Используйте
словарь для хранения информации.
"""

# vocabulary = [
#     {"word": "home", "translate": "domicile"},
#     {"word": "world", "translate": "monde"},
#     {"word": "hello", "translate": "bonjour"}
# ]
#
#
# def add_word_func():
#     word_english = input("Введите слово на английском: ")
#     word_france = input("Введите слово на французком: ")
#     vocabulary.append({"word": word_english, "translate": word_france})
#
#
# def delete_word_func():
#     word_english = input("Введите слово на английском, которое хотите удалить: ")
#     for i in range(len(vocabulary)-1, 0, -1):
#         if vocabulary[i]["word"] == word_english:
#             vocabulary.pop(i)
#
#
# def search_word_func():
#     word_english = input("Введите слово на английском, чтоб перевести его на французский: ")
#     for i in range(0, len(vocabulary)):
#         if vocabulary[i]["word"] == word_english:
#             print(vocabulary[i])
#
#
# def edit_word_func():
#     word_english = input("Введите слово на английском, которого хотите изменить: ")
#     for i in range(0, len(vocabulary)):
#         if vocabulary[i]["word"] == word_english:
#             edit_word_english = input("Введите слово на английском:: ")
#             edit_word_france = input("Введите слово на французком: ")
#             vocabulary[i] = {"word": edit_word_english, "translate": edit_word_france}
#

# while True:
#     controls = input("Введите действие "
#                      "(добавление - 1, удаление - 2, поиск - 3, замена - 4, показать список - 5, "
#                      "закрыть программу - 0): ")
#     if controls == "1":
#         add_word_func()
#     elif controls == "2":
#         delete_word_func()
#     elif controls == "3":
#         search_word_func()
#     elif controls == "4":
#         edit_word_func()
#     elif controls == "5":
#         print(vocabulary)
#     elif controls == "0":
#         exit(0)
#     else:
#         print("Нет такого действия!")
#         continue

"""
Задание 3
Создайте программу «Фирма». Нужно хранить ин-
формацию о человеке: ФИО, телефон, рабочий email,
название должности, номер кабинета, skype. Требуется
реализовать возможность добавления, удаления, поис-
ка, замены данных. Используйте словарь для хранения
информации.
"""

# information = [
#     {"ФИО": "Пупкин Василий Александрович", "телефон": "380985432178", "email": "pupkin.vasya@gmail.com",
#      "должность": "Генеральный директор", "номер кабинета": 401, "skype": "pupkin_vasya.skype"}
# ]
#
#
# def add_employees_func():
#     name = input("Введите ФИО: ")
#     tel = input("Введите телефон: ")
#     email = input("Введите email: ")
#     position = input("Введите должность: ")
#     room_number = input("Введите номер кабинета: ")
#     skype = input("Введите skype: ")
#     information.append({"ФИО": name, "телефон": tel, "email": email,
#                        "должность": position, "номер кабинета": room_number, "skype": skype})
#
#
# def delete_employees_func():
#     name = input("Введите ФИО сотрудника, которого хотите удалить: ")
#     for i in range(len(information)-1, 0, -1):
#         if information[i]["ФИО"] == name:
#             information.pop(i)
#
#
# def search_employees_func():
#     name = input("Введите ФИО сотрудника, чтоб получить информацию о нем: ")
#     for i in range(0, len(information)):
#         if information[i]["ФИО"] == name:
#             print(information[i])
#
#
# def edit_employees_func():
#     name = input("Введите ФИО сотрудника, чтоб изменить информацию о нем: ")
#     for i in range(0, len(vocabulary)):
#         if vocabulary[i]["word"] == name:
#             edit_name = input("Введите ФИО: ")
#             edit_tel = input("Введите телефон: ")
#             edit_email = input("Введите email: ")
#             edit_position = input("Введите должность: ")
#             edit_room_number = input("Введите номер кабинета: ")
#             edit_skype = input("Введите skype: ")
#             information[i] = {"ФИО": edit_name, "телефон": edit_tel, "email": edit_email,
#                                 "должность": edit_position, "номер кабинета": edit_room_number, "skype": edit_skype}
#
#
# while True:
#     controls = input("Введите действие "
#                      "(добавление - 1, удаление - 2, поиск - 3, замена - 4, показать список - 5, "
#                      "закрыть программу - 0): ")
#     if controls == "1":
#         add_employees_func()
#     elif controls == "2":
#         delete_employees_func()
#     elif controls == "3":
#         search_employees_func()
#     elif controls == "4":
#         edit_employees_func()
#     elif controls == "5":
#         print(information)
#     elif controls == "0":
#         exit(0)
#     else:
#         print("Нет такого действия!")
#         continue

"""
Задание 4
Создайте программу «Книжная коллекция». Нужно
хранить информацию о книгах: автор, название книги,
жанр, год выпуска, количество страниц, издательство.
Требуется реализовать возможность добавления, удале-
ния, поиска, замены данных. Используйте словарь для
хранения информации.
"""

# book_collection = [
#     {"author": "Джордж Оруэлл", "book": "1984", "genre": "роман-антиутопия",
#      "year": "1949", "pages": "479", "publishing": "АСТ"}
# ]
#
#
# def add_book_func():
#     author = input("Введите автора: ")
#     book = input("Введите название книги: ")
#     genre = input("Введите жанр: ")
#     year = input("Введите год выпуска: ")
#     pages = input("Введите количество страниц: ")
#     publishing = input("Введите издательство: ")
#     book_collection.append({"author": author, "book": book, "genre": genre,
#                             "year": year, "pages": pages, "publishing": publishing})
#
#
# def delete_book_func():
#     book = input("Введите книгу, которую хотите удалить: ")
#     for i in range(len(book_collection)-1, 0, -1):
#         if book_collection[i]["book"] == book:
#             book_collection.pop(i)
#
#
# def search_book_func():
#     author = input("Введите автора, чтоб получить информацию о его книгах: ")
#     for i in range(0, len(book_collection)):
#         if book_collection[i]["author"] == author:
#             print(book_collection[i])
#
#
# def edit_book_func():
#     book = input("Введите название книги, чтоб отредактировать информацию о ней: ")
#     for i in range(0, len(book_collection)):
#         if book_collection[i]["book"] == book:
#             edit_author = input("Введите автора: ")
#             edit_book = input("Введите название книги: ")
#             edit_genre = input("Введите жанр: ")
#             edit_year = input("Введите год выпуска: ")
#             edit_pages = input("Введите количество страниц: ")
#             edit_publishing = input("Введите издательство: ")
#             book_collection[i] = {"author": edit_author, "book": edit_book, "genre": edit_genre,
#                                   "year": edit_year, "pages": edit_pages, "publishing": edit_publishing}
#
#
# while True:
#     controls = input("Введите действие "
#                      "(добавление - 1, удаление - 2, поиск - 3, замена - 4, показать список - 5, "
#                      "закрыть программу - 0): ")
#     if controls == "1":
#         add_book_func()
#     elif controls == "2":
#         delete_book_func()
#     elif controls == "3":
#         search_book_func()
#     elif controls == "4":
#         edit_book_func()
#     elif controls == "5":
#         print(book_collection)
#     elif controls == "0":
#         exit(0)
#     else:
#         print("Нет такого действия!")
#         continue
